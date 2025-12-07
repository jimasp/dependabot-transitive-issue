"""
Demo script to show Dependabot transitive dependency issue.

This uses dependabot-transitive-demo package which has a transitive
dependency on vulnerable urllib3.
"""

from dependabot_transitive_demo import demo_function

if __name__ == "__main__":
    print("This project demonstrates Dependabot transitive dependency detection.")
    print("Using dependabot-transitive-demo package with vulnerable urllib3 dependency.")
    print()
    demo_function()
