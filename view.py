import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    PAD = 10

    MAX_BUTTONS_PER_ROW = 4
    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title('PyCalculator V1.0')
        self.config(bg='black')
        self._configure_button_styles()

        self.value_var = tk.StringVar()
        self._make_main_frame()
        self._make_label()
        self._make_buttons()
        self._center_window()

    def _configure_button_styles(self):
        style = ttk.Style()
        style.theme_use('alt')

        #style for number buttons
        style.configure('N.TButton', foreground='white', background='gray')
        #style for operator buttons
        style.configure('O.TButton', foreground='white', background='orange')
        #style for miscellaneous buttons
        style.configure('M.TButton', foreground='white', background='gray')


    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _make_label(self):
        label = tk.Label(self.main_frame, anchor='e', textvariable=self.value_var,
                         bg='black', fg='white', font=('Ariel', 30))
        label.pack(fill='x')

    def _make_buttons(self):
        main_frame = ttk.Frame(self.main_frame)
        main_frame.pack()

        is_first_row = True

        buttons_in_row = 0

        for caption in self.button_captions:
            if is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                is_first_row = False

                frame = ttk.Frame(main_frame)
                frame.pack(fill='x')
                buttons_in_row = 0

            if isinstance(caption, int):
                style_prefix = 'N'
            elif self._is_operator(caption):
                style_prefix = 'O'
            else:
                style_prefix = 'M'

            style_name = f'{style_prefix}.TButton'

            button = ttk.Button(frame, text=caption, width=20, style=style_name,
                                command=(lambda button=caption: self.controller.on_button_click(button)))
            if caption == 0:
                fill = 'x'
                expand = 1
            else:
                fill = 'none'
                expand = 0
            button.pack(fill=fill,expand=expand, side='left')
            buttons_in_row += 1

    def _is_operator(self, button_caption):
        return button_caption in ['/', '*', '-', '+', '=']

    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}')
