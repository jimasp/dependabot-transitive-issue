"""
Dependabot Transitive Demo Package

A minimal package for demonstrating Dependabot transitive dependency detection.
"""

__version__ = "1.0.0"

import urllib3

def demo_function():
    """
    A simple demo function that uses urllib3.
    
    This function exists solely to demonstrate that the package uses urllib3
    as a dependency.
    """
    http = urllib3.PoolManager()
    print(f"dependabot-transitive-demo v{__version__}")
    print(f"Using urllib3 v{urllib3.__version__}")
    return "Demo function executed successfully"

__all__ = ["demo_function"]
