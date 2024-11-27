from customtkinter import set_appearance_mode, CTk, CTkLabel, CTkEntry, CTkButton, CTkProgressBar, CTkFrame

# Set the appearance mode of the application (dark mode in this case)
set_appearance_mode("dark")

class Window(CTk):
    """
    A class to create a custom window using the CustomTkinter library.
    This class includes methods to create labels, entry fields, buttons, 
    and manage the user interface lifecycle.
    """

    def __init__(self, title: str = None):
        """
        Initialize the window with a title and a fixed size.
        Configure the grid layout to make rows and columns expandable.
        """
        super().__init__()

        self.title(title)  # Set the window title
        self.geometry(f"{600}x{400}")  # Set the window size

        # Configure grid layout (3x3)
        self.grid_columnconfigure((0, 1, 2), weight=1)  # Make columns expandable
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)  # Make rows expandable

        # Internal variables for widgets
        self.__text_digited = None
        self.__entry = None

    def label(self, text: str = None, row: int = None, column: int = None, 
              padY: tuple = None, padX: tuple = None, sticky: str = None, size_font: str = None):
        """
        Create a label and place it in the specified grid location.

        Args:
            text (str): Text to display in the label.
            row, column (int): Grid row and column for the label.
            padY, padX (tuple): Padding for the label.
            sticky (str): Alignment of the label.
            size_font (str): Font size of the label.
        """
        self.__label = CTkLabel(
            master=self, text=text, font=("Arial", size_font)
        )
        self.__label.grid(row=row, column=column, padx=padX, pady=padY, sticky=sticky)

    def entry(self, text: str = None, width: int = None, row: int = None, 
              column: int = None, padY: tuple = None, padX: tuple = None, sticky: str = None):
        """
        Create an entry field with a placeholder and place it in the specified grid location.
        """
        self.__entry = CTkEntry(
            master=self, placeholder_text=text, width=width, 
            fg_color="gray10", text_color='White', font=("Arial", 12, "bold")
        )
        self.__entry.grid(row=row, column=column, padx=padX, pady=padY, sticky=sticky)

    def button(self, text: str = None, row: int = None, column: int = None, 
               padY: tuple = None, padX: tuple = None, width: int = None, 
               height: int = None, command=None):
        """
        Create a button with customizable text and command action, and place it in the grid.
        """
        self.__button = CTkButton(
            master=self, fg_color="#FF69B4", border_width=2, 
            text_color=("gray10", "#DCE4EE"), width=width, height=height, 
            text=text, command=command
        )

        # Make the grid cells uniform
        self.__button.grid_columnconfigure(column, weight=1, uniform="equal")
        self.__button.grid_rowconfigure(row, weight=1, uniform="equal")

        self.__button.grid(row=row, column=column, padx=padX, pady=padY)

    def show_text(self) -> None:
        """Retrieve and store the text entered in the entry field."""
        if self.__entry:
            self.__text_digited = self.__entry.get()

    def destroy(self):
        """
        Override the default destroy method to safely capture the entered text
        and close the window after the current event cycle.
        """
        try:
            self.show_text()  # Capture the entered text
            self.after(0, self._safe_destroy)  # Ensure the event cycle completes before destruction
        except Exception:
            pass

    def _safe_destroy(self):
        """Safely destroy the window to avoid exceptions during closing."""
        try:
            super().destroy()
        except Exception:
            pass

    def press_key(self, event: str = None):
        """Handle key press events and close the window on Enter key."""
        self.show_text()
        if event == 'Return':
            self.destroy()

    def close(self):
        """Close the window."""
        self.destroy()

    def wait(self, text: str = None):
        """
        Display a loading message and an indeterminate progress bar.
        Used to indicate that a process is running.
        """
        self.label(text, 0, 1, (10, 10), (10, 10), 'ew', 20)

        # Create a progress bar frame
        self.slider_progressbar_frame = CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(
            row=2, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew"
        )
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)

        # Add a progress bar
        self.progressbar_1 = CTkProgressBar(self.slider_progressbar_frame, width=400)
        self.progressbar_1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1.configure(mode="indeterminate")
        self.progressbar_1.start()

    def window_recursive(self, text: str = None, text_entry: str = None):
        """
        Create a window that allows the user to input text through an entry field.
        """
        self.label(text, 0, 1, (10, 10), (10, 10), 'ew', 15)
        self.entry(text_entry, 500, 1, 1, (10, 10), (10, 10), 'ew')

        self.button('Send', 3, 1, (10, 10), (10, 10), 100, 35, self.destroy)
        
        # Bind the Enter key to trigger the text capture and window closing
        self.__entry.bind("<KeyPress>", self.press_key)

        self.mainloop()
        return self.__text_digited

    def fineshed(self, text: str = None):
        """
        Display a message indicating the process has finished and provide an 'OK' button to close the window.
        """
        self.label(text, 1, 1, (10, 10), (10, 10), 'ew', 20)
        self.button('OK', 3, 1, (10, 10), (10, 10), 100, 35, self.destroy)
        self.mainloop()
