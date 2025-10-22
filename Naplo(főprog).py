from tkinter import Tk
import myapp as m


def main():
    try:
        cald = Tk()
        m.Myapp(cald)
        cald.geometry("1050x720")
        cald.resizable(0, 0)
        cald.title("Hataridonaplo")
        cald.mainloop()
    except:
        print("Hiba")


main()
# https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
# https://www.youtube.com/watch?v=i4qLI9lmkqw&t
# https://docs.python.org/3.9/library/csv.html
# https://www.programiz.com/python-programming/class
# https://www.youtube.com/watch?v=VT8hV6rH4Gk
# https://blog.finxter.com/how-to-convert-a-list-of-lists-to-a-csv-file-in-python/
# https://www.codevscolor.com/date-valid-check-python
