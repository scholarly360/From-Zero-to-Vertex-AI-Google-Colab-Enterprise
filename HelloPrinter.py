class HelloPrinter:
    """A simple class to print hello messages."""
    
    def __init__(self, name="World"):
        """
        Initialize the HelloPrinter with a name.
        
        Args:
            name (str): The name to greet. Defaults to "World".
        """
        self.name = name
    
    def print_hello(self):
        """Print a hello message."""
        print(f"Hello, {self.name}!")
    
    def print_custom_message(self, message):
        """
        Print a custom message with the name.
        
        Args:
            message (str): Custom message to print.
        """
        print(f"{message}, {self.name}!")