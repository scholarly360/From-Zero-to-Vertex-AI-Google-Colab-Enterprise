import jupytext
import nbformat
from nbformat.v4 import new_code_cell

# Read the Python file and convert it to a notebook
notebook = jupytext.read('HelloPrinter.py')

# Add a new code cell to demonstrate using the HelloPrinter class
demo_code = """# Demo: Using the HelloPrinter class
printer2 = HelloPrinter()
printer2.print_hello()"""

new_cell = new_code_cell(demo_code)
notebook.cells.append(new_cell)

# Write the notebook to a .ipynb file
jupytext.write(notebook, 'HelloPrinter.ipynb')

print("Successfully converted HelloPrinter.py to HelloPrinter.ipynb")
print("\nNotebook structure:")
print(f"Number of cells: {len(notebook.cells)}")
for i, cell in enumerate(notebook.cells):
    print(f"Cell {i+1}: {cell.cell_type}")