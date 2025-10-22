import reading as r


def name_search():
    name_list = []
    for item in r.Reading():
        if item._name.lower().replace(" ", "").strip() not in name_list:
            name_list.append(
                item._name.lower().replace(" ", "").strip())
    return name_list
