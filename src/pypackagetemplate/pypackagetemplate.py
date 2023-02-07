"""Docstring of Module
"""


class PyPackageTemplate:
    """Docstring of PyPackageTemplate"""

    def __init__(self) -> None:
        print("init func of class")

    def public_method(self, var1: int) -> int:
        """Public method docstring."""
        print("public method with input argument ", var1)
        return var1

    def add_vars(self, var1: float, var2: float) -> float:
        """adds var1 and var2"""
        return var1 + var2
