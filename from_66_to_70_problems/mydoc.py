import importlib
import inspect
import sys

def print_module_doc(module_name):
    try:
        module = importlib.import_module(module_name)
        print(f"Documentation for module:", {module_name})
        print(module.__doc__)
        print()

        functions = inspect.getmembers(module, inspect.isfunction)
        for name, function in functions:
            print(f"Documentation for function:", {name})
            print(function.__doc__)
            print()

    except ImportError:
        print(f"Module '{module_name}' not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python print_module_doc.py <module_name>")
        sys.exit()
    else:
        module_name = sys.argv[1]
        print_module_doc(module_name)