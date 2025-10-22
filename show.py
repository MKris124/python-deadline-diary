from tkinter.constants import BOTTOM, NE, NW, SW, TOP, Y, E, END
import myapp as m


def show():
    m.update_list()
    m.drop.pack(side=TOP, anchor=NE)
    m.sorterer.pack(side=TOP, anchor=NE)
    m.Search_add_part.pack(fill="both", expand="yes", padx=20, pady=10)
    m.trv.pack(side=TOP, anchor=NW, fill=Y)
    m.day_event_list.pack(side=BOTTOM, anchor=SW)
    m.Calendar_part.pack(fill="both", expand="yes", padx=20, pady=10)
    m.show_everything.pack_forget()
    m.search_lbl.grid(row=0, column=2, padx=5, pady=3)
    m.search_entry.grid(row=0, column=3, padx=5, pady=3)
    m.search_btn.grid(row=0, column=4, padx=5, pady=3)
    m.add_delete_name_label.grid(
        row=0, column=0, sticky=E, padx=5, pady=3)
    m.add_delete_date_label.grid(row=1, column=0, padx=5, pady=3)
    m.add_delete_time_label.grid(row=2, column=0, padx=5, pady=3)
    m.add_delete_place_label.grid(row=3, column=0, padx=5, pady=3)
    m.add_delete_other_label.grid(row=4, column=0, padx=5, pady=3)

    m.add_delete_name_entry.grid(row=0, column=1, padx=5, pady=3)
    m.add_delete_date_entry.grid(row=1, column=1, padx=5, pady=3)
    m.add_delete_time_entry.grid(row=2, column=1, padx=5, pady=3)
    m.add_delete_place_entry.grid(row=3, column=1, padx=5, pady=3)
    m.add_delete_other_entry.grid(row=4, column=1, padx=5, pady=3)

    m.delete_item.grid(row=1, column=2, padx=5, pady=3)
    m.add_item.grid(row=2, column=2, padx=5, pady=3)
    m.update_item.grid(row=3, column=2, padx=5, pady=3)
    m.export_item.grid(row=0, column=5, padx=5, pady=3)
    m.error.grid(row=0, column=6, padx=5, pady=5)
