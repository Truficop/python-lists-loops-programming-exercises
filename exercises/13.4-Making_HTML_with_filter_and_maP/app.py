all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def filter_colors(colores):
    filtered_colors = list(filter(lambda color: color["sexy"] == True, colores))
    return filtered_colors

sexy_colors = filter_colors(all_colors)

def generate_li(colores):
    new_list = list(map(lambda color: f"<li>{color['label']}</li>", colores))
    return new_list

print(generate_li(sexy_colors))