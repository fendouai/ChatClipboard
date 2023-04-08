import tkinter as tk
import pyperclip
import openai

openai.api_key = 'sk-your key'

class App:
    def __init__(self, master):
        self.master = master
        master.title("ChatClipboard")

        self.label = tk.Label(master, text="Chat by Clipboard")
        self.label.pack()

        self.result_box = tk.Text(master, height=10, width=50)
        self.result_box.pack()

        self.my_button = tk.Button(master, text="Button", command=self.check_clipboard)
        self.my_button.pack()

    def check_clipboard(self):
        question = pyperclip.paste()

        self.label.config(text=question)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        output_text = response.choices[0].message["content"]
        pyperclip.copy(output_text)
        self.result_box.config(text=output_text)


root = tk.Tk()
app = App(root)
root.mainloop()
