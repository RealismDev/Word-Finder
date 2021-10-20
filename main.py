from tkinter import *
from random import choice
defaultColor = "#3E4442"
defaultWidgetColor = "#595F5D"
root = Tk()
root.title("Word finder")
root.configure(bg=defaultColor)
root.geometry("500x250")
root.resizable(0, 0)


def loadWords():
    try:
        with open("words.txt") as file:
            words = set(file.read().split())

        return words
    except FileNotFoundError:
        a = Label(root, text="words.txt not found.", bg='RED')
        a.pack()


englishWords = loadWords()


def doesWordContain(word, sequence):
    if not word.lower().find(sequence.lower()) == -1:
        return True
    else:
        return False


def getWordsContaining(sequence):
    foundWords = []
    try:
        for word in englishWords:
            WordContains = doesWordContain(word, sequence)
            if WordContains:
                foundWords.append(word)
    except TypeError:
        pass
    return foundWords


def main():
    sequenceEntry = Entry(root, width=30, borderwidth=2, bg="#DFE4E2")
    sequenceEntry.place(relx=0.5, rely=0.2, anchor=CENTER)
    sequenceEntry.insert(0, "Insert sequence here!")

    foundWordText = Label(root, text="Found word will appear here.",
                          padx=15, pady=5, bg=defaultWidgetColor, fg="white")
    foundWordText.place(relx=0.5, rely=0.7, anchor=CENTER)

    getWordbutton = Button(root, text="Get word with sequence",
                           command=lambda: getWordClicked(sequenceEntry.get(), foundWordText), padx=15, pady=5, bg=defaultWidgetColor, fg="white")
    getWordbutton.place(relx=0.5, rely=0.4, anchor=CENTER)

    root.mainloop()


def getWordClicked(sequence, textToUpd):
    foundWords = getWordsContaining(sequence)

    foundWordsLength = len(foundWords)

    if not foundWordsLength == 0:
        # There are words
        randomWord = choice(foundWords)
        textToUpd.config(
            text=f"Your word is '{randomWord}' with {foundWordsLength} entries containing {sequence}")
    else:
        textToUpd.config(text=f"No words found containing '{sequence}'")


if __name__ == '__main__':
    main()
