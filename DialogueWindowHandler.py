from tkinter import filedialog

class DialogueWindow:
    def FileOpen():
        fTyp = [("", "csv")]
        iFilePath = filedialog.askopenfilename(filetype = fTyp)
        return iFilePath
