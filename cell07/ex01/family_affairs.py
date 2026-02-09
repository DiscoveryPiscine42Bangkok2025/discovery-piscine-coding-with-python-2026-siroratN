def find_the_redheads(names_dict):
    
    redheads = filter(lambda name: names_dict[name].lower() == "red", names_dict.keys())
    
    return list(redheads)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))