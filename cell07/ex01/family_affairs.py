


def find_the_redheads(names_dict):
    
    def find_redhead(i):
        return names_dict[i].lower() == "red"
    
    redheads = filter(find_redhead, names_dict.keys())
    
    return list(redheads)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))