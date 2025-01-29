
from promptflow import tool
import sympy as sp
import re
# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str) -> str:
    """
    Function to process math-related questions, adjust notation from user-friendly to Python-friendly,
    and return explanations along with LaTeX-formatted results.
    """
    try:
        # Clean the expression and replace '^' with '**' for proper Python syntax
        cleaned_expression = input1.replace("^", "**")
        math_expression = re.findall(r'[0-9a-zA-Z+\-*/().∫√\s]+', cleaned_expression)
        
        if not math_expression:
            return "No valid mathematical expression found."

        # Assume the first valid expression is what we need to process
        expression_to_parse = math_expression[0]
        sympy_expression = sp.sympify(expression_to_parse)

        # Generate an explanation based on detected mathematical operations
        explanation = "The expression simplifies to:"
        latex_result = f"$$ {sp.latex(sympy_expression)} $$"

        return explanation + " " + latex_result

    except sp.SympifyError:
        return 'hello ' + input1
