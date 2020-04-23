HEX_CODES = {"DarkSlateGray1": "#97ffff", "DarkGoldenrod2": "#eead0e","AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc", "CadetBlue3": "#7ac5cd", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b", "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

colour_name = input("Enter the name of the colour: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             HEX_CODES.get(colour_name)))
    colour_name = input("Enter the name of the colour: ")
