def generateFolderIcon(color):
    with open('generated/folder-' + color + '.svg', 'w') as f:
        f.write("""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
        <defs id="defs3051">
            <style type="text/css" id="current-color-scheme">
            .ColorScheme-Text {
                color:""" + color + """;
            }
            .ColorScheme-Highlight {
                color:#3daee9;
            }
            </style>
        </defs>
        <path 
            style="fill:""" + color + """" 
            d="M 4 6 L 4 11 L 4 20 L 3 20 L 3 21 L 3 21 C 3 21 3 21 3 21 L 3 57 L 3 58 L 4 58 L 60 58 L 61 58 L 61 57 L 61 21 L 61 21 L 61 16 L 60 16 L 60 11 C 60 11 60 11 60 11 L 60 11 L 60 10 L 32 10 L 28 6 L 4 6 z "
            />
        <path 
            style="fill-opacity:0.33"
            d="M 4 6 L 4 11 L 4 20 L 22 20 L 26 16 L 60 16 L 60 11 C 60 11 60 11 60 11 L 60 11 L 60 10 L 32 10 L 28 6 L 4 6 z "
            />
        <path 
            style="fill:#ffffff;fill-opacity:0.2"
            d="M 28 6 L 31 11 L 33 11 L 60 11 L 60 10 L 33 10 L 32 10 L 28 6 z M 26 16 L 22 20 L 3 20 L 3 21 L 23 21 L 26 16 z "
            />
        <path 
            style="fill-opacity:0.2;fill-rule:evenodd"
            d="M 26 16 L 20 19 L 4 19 L 4 20 L 22 20 L 26 16 z M 3 57 L 3 58 L 4 58 L 60 58 L 61 58 L 61 57 L 60 57 L 4 57 L 3 57 z "
            class="ColorScheme-Text"
            />
    </svg>
    """)
        f.close()

def h(int):
    return hex(int).replace('0x','') * 2

for r in range(0, 16, 2):
    for g in range(0, 16, 2):
        for b in range(0, 16, 2):
            color = '#' + h(r) + h(g) + h(b)
            generateFolderIcon(color)