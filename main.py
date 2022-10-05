import colorgram

colors = colorgram.extract('painting.webp', 10)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    
print(rgb_colors)
