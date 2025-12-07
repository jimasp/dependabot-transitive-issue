"""
Simple script to demonstrate Dependabot transitive dependency issue.
This project uses jupyter-server which has transitive dependencies.
"""


def main():
    """Main function."""
    print("This project demonstrates Dependabot transitive dependency detection.")
    print("Check requirements.txt for the dependency configuration.")
    
    # Import to verify the package works
    try:
        import jupyter_server
        print(f"jupyter-server version: {jupyter_server.__version__}")
    except ImportError:
        print("jupyter-server not installed. Run: pip install -r requirements.txt")


if __name__ == '__main__':
    main()
