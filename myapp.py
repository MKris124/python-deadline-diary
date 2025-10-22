from tkinter import Button, Entry, Label, font
from tkinter.constants import BOTTOM, NE, NW, SW, TOP, Y, E, END
import sorter as sort
import searching as search
from tkinter import StringVar, LabelFrame, OptionMenu, Listbox, ttk
import months_to_index as m
import sorter_to_index as s
import reading as r
import pandas as pd
import datetime as dt


class Myapp:
    def __init__(self, master):
        self.sel = StringVar(value=list(m.months_to_index)[0])
        self.sel2 = StringVar(value=list(s.sorter_to_index)[0])
        self.Calendar_part = LabelFrame(master, text="Calendar")
        self.Search_add_part = LabelFrame(master, text="Search-Add-Delete")
        self.drop = OptionMenu(self.Calendar_part, self.sel,
                               *m.months_to_index.keys(), command=self.selected)

        self.sorterer = OptionMenu(self.Calendar_part, self.sel2,
                                   *s.sorter_to_index.keys(), command=self.sorted_list_by)

        self.trv = ttk.Treeview(self.Calendar_part, columns=(1, 2, 3, 4, 5, 6),
                                show="headings", height="10")

        self.trv.heading(1, text="Név", command=self.sorted_name)
        self.trv.heading(2, text="Dátum", command=self.sorted_date)
        self.trv.heading(3, text="Idő", command=self.sorted_time)
        self.trv.heading(4, text="Hely")
        self.trv.heading(5, text="Egyéb")
        self.trv.heading(6)
        self.trv.column("#6", stretch=False, width=0)
        self.trv.column("#2", anchor="center")
        self.trv.column("#3", anchor="center")
        self.trv.bind('<ButtonRelease-1>', self.selected_to_list)
        self.trv.bind('<Double-1>', self.get_selected_information)
        self.day_event_list = Listbox(self.Calendar_part, width=50,
                                      height=10)

        self.search_lbl = Label(self.Search_add_part, text="Keresés")

        self.search_entry = Entry(self.Search_add_part, textvariable="")

        self.search_btn = Button(self.Search_add_part,
                                 command=self.list_searched, text="Keresés")
        self.show_everything = Button(master, command=self.show, text="Kezdés")
        self.show_everything.pack()

        self.add_delete_name_label = Label(self.Search_add_part, text="Név")
        self.add_delete_date_label = Label(self.Search_add_part, text="Dátum")
        self.add_delete_time_label = Label(self.Search_add_part, text="Idő")
        self.add_delete_place_label = Label(self.Search_add_part, text="Hely")
        self.add_delete_other_label = Label(self.Search_add_part, text="Egyéb")
        self.add_delete_other_entry = Entry(
            self.Search_add_part, textvariable="")
        self.add_delete_place_entry = Entry(
            self.Search_add_part, textvariable="")
        self.add_delete_time_entry = Entry(
            self.Search_add_part, textvariable="")
        self.add_delete_date_entry = Entry(
            self.Search_add_part, textvariable="")
        self.add_delete_name_entry = Entry(
            self.Search_add_part, textvariable="")
        self.id_entry = Entry(self.Search_add_part, textvariable="")

        self.add_delete_other_entry1 = Entry(
            self.Search_add_part, textvariable="")
        self.add_delete_place_entry1 = Entry(
            self.Search_add_part, textvariable="")
        self.add_delete_time_entry1 = Entry(
            self.Search_add_part, textvariable="")
        self.add_delete_date_entry1 = Entry(
            self.Search_add_part, textvariable="")
        self.add_delete_name_entry1 = Entry(
            self.Search_add_part, textvariable="")
        self.id_entry1 = Entry(self.Search_add_part, textvariable="")

        self.delete_item = Button(
            self.Search_add_part, text="Törlés", command=self.delete_update)
        self.add_item = Button(self.Search_add_part, text="Hozzáadás",
                               command=self.add_item_command)
        self.update_item = Button(self.Search_add_part, text="Módosítás",
                                  command=self.update_item_command)
        self.export_item = Button(self.Search_add_part, text="Export csv-be",
                                  command=self.export_to_csv)

        self.error = Label(self.Search_add_part, text="")

        self.list_btn = Button(self.Search_add_part, text="Újralistáz",
                               command=self.update_list)

    def show(self):
        self.update_list()
        self.drop.pack(side=TOP, anchor=NE)
        self.sorterer.pack(side=TOP, anchor=NE)
        self.Search_add_part.pack(fill="both", expand="yes", padx=20, pady=10)
        self.trv.pack(side=TOP, anchor=NW, fill=Y)
        self.day_event_list.pack(side=BOTTOM, anchor=SW)
        self.Calendar_part.pack(fill="both", expand="yes", padx=20, pady=10)
        self.show_everything.pack_forget()
        self.search_lbl.grid(row=0, column=2, padx=5, pady=3)
        self.search_entry.grid(row=0, column=3, padx=5, pady=3)
        self.search_btn.grid(row=0, column=4, padx=5, pady=3)
        self.add_delete_name_label.grid(
            row=0, column=0, sticky=E, padx=5, pady=3)
        self.add_delete_date_label.grid(row=1, column=0, padx=5, pady=3)
        self.add_delete_time_label.grid(row=2, column=0, padx=5, pady=3)
        self.add_delete_place_label.grid(row=3, column=0, padx=5, pady=3)
        self.add_delete_other_label.grid(row=4, column=0, padx=5, pady=3)

        self.add_delete_name_entry.grid(row=0, column=1, padx=5, pady=3)
        self.add_delete_date_entry.grid(row=1, column=1, padx=5, pady=3)
        self.add_delete_time_entry.grid(row=2, column=1, padx=5, pady=3)
        self.add_delete_place_entry.grid(row=3, column=1, padx=5, pady=3)
        self.add_delete_other_entry.grid(row=4, column=1, padx=5, pady=3)

        self.delete_item.grid(row=1, column=2, padx=5, pady=3)
        self.add_item.grid(row=2, column=2, padx=5, pady=3)
        self.update_item.grid(row=3, column=2, padx=5, pady=3)
        self.export_item.grid(row=0, column=5, padx=5, pady=3)
        self.error.grid(row=0, column=6, padx=5, pady=5)

    def sorted_name(self):
        for item in self.trv.get_children():
            self.trv.delete(item)
        sorted_list = sorted(r.Reading(), key=sort.sorted_by_name)
        for i in sorted_list:
            self.trv.insert('', 'end', values=(
                i._name,
                i._date,
                i._time,
                i._place,
                i._other,
                i._id),)

    def sorted_date(self):
        for item in self.trv.get_children():
            self.trv.delete(item)
        sorted_list = sorted(r.Reading(), key=sort.sorted_by_date)
        for i in sorted_list:
            self.trv.insert('', 'end', values=(
                i._name,
                i._date,
                i._time,
                i._place,
                i._other,
                i._id),)

    def sorted_time(self):
        for item in self.trv.get_children():
            self.trv.delete(item)
        sorted_list = sorted(r.Reading(), key=sort.sorted_by_time)
        for i in sorted_list:
            self.trv.insert('', 'end', values=(
                i._name,
                i._date,
                i._time,
                i._place,
                i._other,
                i._id),)

    def sorted_list_by(self, event):
        for item in self.trv.get_children():
            self.trv.delete(item)
        selected_month = m.months_to_index[self.sel.get()]
        selected_sort = s.sorter_to_index[self.sel2.get()]
        if selected_sort == 1:
            sorted_list = sorted(r.Reading(), key=sort.sorted_by_name)
        elif selected_sort == 2:
            sorted_list = sorted(r.Reading(), key=sort.sorted_by_date)
        elif selected_sort == 3:
            sorted_list = sorted(r.Reading(), key=sort.sorted_by_time)
        for i in sorted_list:
            date_month = i._date.split(".")[1]
            if int(date_month) == selected_month:
                self.trv.insert('', 'end', values=(
                    i._name,
                    i._date,
                    i._time,
                    i._place,
                    i._other,
                    i._id),)

    def selected(self, event):
        for item in self.trv.get_children():
            self.trv.delete(item)
        selected_month = m.months_to_index[self.sel.get()]
        for i in r.Reading():
            date_month = i._date.split(".")[1]
            if int(date_month) == selected_month:
                self.trv.insert('', 'end', values=(
                    i._name,
                    i._date,
                    i._time,
                    i._place,
                    i._other,
                    i._id))
        self.list_btn.grid(row=1, column=5, padx=5, pady=3)

    def update_list(self):
        for item in self.trv.get_children():
            self.trv.delete(item)
        sorted_list = sorted(r.Reading(), key=sort.sorted_by_id)
        for i in sorted_list:
            self.trv.insert('', 'end', values=(
                i._name,
                i._date,
                i._time,
                i._place,
                i._other,
                i._id))
        self.list_btn.grid_forget()

    def selected_to_list(self, event):
        self.day_event_list.delete(0, "end")
        sorted_list = sorted(r.Reading(), key=sort.sorted_by_time)
        for item in self.trv.selection():
            item_date = self.trv.item(item, "values")[1]
            for line in sorted_list:
                if line._date == item_date:
                    self.day_event_list.insert(
                        END, f"{line._time}\n {line._name}")

    def searching(self):
        try:
            searching = self.search_entry.get()
            if searching.replace(" ", "") == "":
                raise TypeError
            searched_thing = []
            for i in search.name_search():
                if searching.lower().strip().replace(" ", "") in i:
                    searched_thing.append(i)
            return searched_thing
        except TypeError:
            self.error.config(text="")
            self.error.config(text="Nem írtál be semmit", foreground="red")
            self.update_list()

    def list_searched(self):
        self.error.config(text="")
        for item in self.trv.get_children():
            self.trv.delete(item)
        sorted_list = sorted(r.Reading(), key=sort.sorted_by_date)
        for i in sorted_list:
            try:
                if len(self.searching()) == 0:
                    raise ValueError
                for j in self.searching():
                    if i._name.lower().replace(" ", "") == j:
                        self.trv.insert('', 'end', values=(
                            i._name,
                            i._date,
                            i._time,
                            i._place,
                            i._other,
                            i._id),)
                        self.list_btn.grid(row=1, column=5, padx=5, pady=3)

            except TypeError:
                self.error.config(text="")
                self.error.config(text="Nem írtál be semmit", foreground="red")
                self.update_list()

            except ValueError:
                self.error.config(text="")
                self.error.config(
                    text="Nincs ilyen nevű esemény.", foreground="red")
                self.update_list()

    def clear_entry(self):
        self.add_delete_name_entry.delete(0, END)
        self.add_delete_date_entry.delete(0, END)
        self.add_delete_time_entry.delete(0, END)
        self.add_delete_place_entry.delete(0, END)
        self.add_delete_other_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.add_delete_name_entry1.delete(0, END)
        self.add_delete_date_entry1.delete(0, END)
        self.add_delete_time_entry1.delete(0, END)
        self.add_delete_place_entry1.delete(0, END)
        self.add_delete_other_entry1.delete(0, END)
        self.id_entry1.delete(0, END)

    def get_selected_information(self, event):
        self.clear_entry()
        for item in self.trv.selection():
            self.add_delete_name_entry.insert(
                0, self.trv.item(item, "values")[0])
            self.add_delete_date_entry.insert(
                0, self.trv.item(item, "values")[1])
            self.add_delete_time_entry.insert(
                0, self.trv.item(item, "values")[2])
            self.add_delete_place_entry.insert(
                0, self.trv.item(item, "values")[3])
            self.add_delete_other_entry.insert(
                0, self.trv.item(item, "values")[4])
            self.id_entry.insert(0, self.trv.item(item, "values")[5])
            self.add_delete_name_entry1 .insert(
                0, self.trv.item(item, "values")[0])
            self.add_delete_date_entry1 .insert(
                0, self.trv.item(item, "values")[1])
            self.add_delete_time_entry1.insert(
                0, self.trv.item(item, "values")[2])
            self.add_delete_place_entry1.insert(
                0, self.trv.item(item, "values")[3])
            self.add_delete_other_entry1.insert(
                0, self.trv.item(item, "values")[4])
            self.id_entry1.insert(0, self.trv.item(item, "values")[5])

    def delete_item_command(self):
        try:
            item_to_delete1 = self.add_delete_name_entry.get()
            item_to_delete2 = self.add_delete_date_entry.get()
            item_to_delete3 = self.add_delete_time_entry.get()
            item_to_delete4 = self.add_delete_place_entry.get()
            item_to_delete5 = self.add_delete_other_entry.get()
            item_to_delete6 = self.id_entry1.get()
            if (item_to_delete1.replace(' ', '') == "" or item_to_delete2.replace(' ', '') == ""
                or item_to_delete3.replace(' ', '') == "" or item_to_delete4.replace(' ', '') == ""
                    or item_to_delete5.replace(' ', '') == "" or item_to_delete6.replace(' ', '') == ""):
                raise ValueError
            to_delete = f"{item_to_delete6}, {item_to_delete1}, {item_to_delete2}, {item_to_delete3}, {item_to_delete4}, {item_to_delete5}\n"
            for item in r.Reading():
                if item_to_delete6 == item._id:
                    for i in self.trv.selection():
                        self.trv.delete(i)
            try:
                with open("adatok.txt", "r", encoding="utf-8") as read:
                    lines = read.readlines()
                read.close()
                with open("adatok.txt", "w", encoding="utf-8") as write:
                    for rows in lines:
                        if rows.replace(" ", "") != to_delete.replace(" ", ""):
                            write.write(rows.replace('\n', ""))
                            write.write('\n')
                    write.close()
            except FileExistsError:
                print("Fájlkezelési hiba")
            self.error.config(
                text="Sikeres törlés", fg='green')
        except ValueError:
            self.error.config(text="")
            self.error.config(
                text="Valamelyik beviteli mező üres.\nNem lehet törölni a sort.\nKattints 2x a táblázatban arra, amelyiket szeretnéd módosítani", foreground="red")

    def delete_update(self):
        self.delete_item_command()
        self.clear_entry()
        self.update_list()

    def add_item_command(self):
        try:
            if (self.add_delete_name_entry.get().replace(' ', '') == "" or self.add_delete_date_entry.get().replace(' ', '') == ""
                    or self.add_delete_time_entry.get().replace(' ', '') == "" or self.add_delete_place_entry.get().replace(' ', '') == ""
                    or self.add_delete_other_entry.get().replace(' ', '') == ""):
                raise TypeError
            year, month, day = self.add_delete_date_entry.get().split('.')
            isdate = True
            if year == "00" or month == "00" or day == "00":
                raise ValueError
            try:
                dt.datetime(int(year), int(month), int(day))
            except ValueError:
                isdate = False
            if isdate == True:
                self.trv.insert('', 'end', values=(
                    self.add_delete_name_entry.get(),
                    self.add_delete_date_entry.get(),
                    self.add_delete_time_entry.get(),
                    self.add_delete_place_entry.get(),
                    self.add_delete_other_entry.get(),
                    self.id_entry.get()
                ))
                id_list = []
                for i in r.Reading():
                    id_list.append(int(i._id))
                row = f"{max(id_list)+1},{self.add_delete_name_entry.get()},{self.add_delete_date_entry.get()},{self.add_delete_time_entry.get()},{self.add_delete_place_entry.get()},{self.add_delete_other_entry.get()}"
                try:
                    with open("adatok.txt", "a", encoding="utf-8") as write:
                        write.write(row)
                        write.write('\n')
                    write.close
                except FileExistsError:
                    print("Fájlkezelési hiba")
                self.clear_entry()
                self.update_list()
                self.error.config(
                    text="Sikeres hozzáadás", fg='green')
        except TypeError:
            self.error.config(text="")
            self.error.config(
                text="Valamelyik beviteli mező üres.\n(az utolsó 3 értékhez elég egy '-' is)")
        except ValueError:
            self.error.config(text="")
            self.error.config(
                text="Nem jól adtad meg a dátumot.\n('Év.hónap.nap' formátumban add meg)", fg='red')

    def update_item_command(self):
        self.error.config(text="")
        try:
            if (self.add_delete_name_entry1.get() == "" or self.add_delete_date_entry1.get() == ""
                    or self.add_delete_time_entry1.get() == "" or self.add_delete_place_entry1.get() == ""
                    or self.add_delete_other_entry1.get() == "" or self.id_entry1.get() == ""):
                raise TypeError
            year, month, day = self.add_delete_date_entry.get().split('.')
            if year == "00" or month == "00" or day == "00":
                raise ValueError
            isdate = True
            try:
                dt.datetime(int(year), int(month), int(day))
            except ValueError:
                isdate = False
            if isdate == True:
                for i in r.Reading():
                    if i._id == self.id_entry.get():
                        item_to_delete1 = self.add_delete_name_entry1.get()
                        item_to_delete2 = self.add_delete_date_entry1.get()
                        item_to_delete3 = self.add_delete_time_entry1.get()
                        item_to_delete4 = self.add_delete_place_entry1.get()
                        item_to_delete5 = self.add_delete_other_entry1.get()
                        item_to_delete6 = self.id_entry1.get()
                        to_delete = f"{item_to_delete6}, {item_to_delete1}, {item_to_delete2}, {item_to_delete3}, {item_to_delete4}, {item_to_delete5}\n"
                        for item in r.Reading():
                            if item_to_delete6 == item._id:
                                for i in self.trv.selection():
                                    self.trv.delete(i)
                        try:
                            with open("adatok.txt", "r", encoding="utf-8") as read:
                                lines = read.readlines()
                                read.close()
                            with open("adatok.txt", "w", encoding="utf-8") as write:
                                for rows in lines:
                                    if rows.replace(" ", "") != to_delete.replace(" ", ""):
                                        write.write(rows.replace('\n', ""))
                                        write.write('\n')
                                write.close()
                        except FileExistsError:
                            print('Fájlkezelési hiba')
                        self.trv.insert('', 'end', values=(
                            self.add_delete_name_entry.get(),
                            self.add_delete_date_entry.get(),
                            self.add_delete_time_entry.get(),
                            self.add_delete_place_entry.get(),
                            self.add_delete_other_entry.get(),
                            self.id_entry.get()
                        ))
                row = f"{self.id_entry.get()},{self.add_delete_name_entry.get()},{self.add_delete_date_entry.get()},{self.add_delete_time_entry.get()},{self.add_delete_place_entry.get()},{self.add_delete_other_entry.get()}"
                try:
                    with open("adatok.txt", "a", encoding="utf-8") as write:
                        write.write(row)
                        write.write('\n')
                    write.close()
                except FileExistsError:
                    print("Fájlkezelési hiba")
                self.clear_entry()
                self.update_list()
                self.error.config(
                    text="Sikeres módosítás", fg='green')
        except TypeError:
            self.error.config(text="")
            self.error.config(
                text="Nincs módosítani kívánt érték\nKattints 2x a táblázatban arra, amelyiket szeretnéd módosítani", fg='red')
        except ValueError:
            self.error.config(text="")
            self.error.config(
                text="Nem jól adtad meg a dátumot.\n('Év.hónap.nap' formátumban add meg)", fg='red')

    def export_to_csv(self):
        data_to_export = []
        headers = ['ID', 'Név', 'Dátum', 'Idő', 'Hely', 'Egyéb']
        sorted_list = sorted(r.Reading(), key=sort.sorted_by_id)
        for i in sorted_list:
            data_to_export.append(
                [i._id, i._name, i._date, i._time, i._place, i._other])
        dataf = pd.DataFrame(data_to_export)
        dataf.to_csv('adatok.csv', index=False, header=headers,
                     sep=';', encoding='utf-8-sig')
        self.error.config(text="")
        self.error.config(
            text="Sikeres exportálás", foreground='green')
