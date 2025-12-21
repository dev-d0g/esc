import pcbnew

new_width_mm = 0.75
new_height_mm = 0.75

board = pcbnew.GetBoard()

for footprint in board.GetFootprints():
    refdes = footprint.GetReference()
    if refdes.startswith("U"):
        continue
    
    for text in footprint.GraphicalItems():
        if isinstance(text, pcbnew.PCB_TEXT):
            size = text.GetTextSize()
            size.x = pcbnew.FromMM(new_height_mm)
            size.y = pcbnew.FromMM(new_width_mm)
            text.SetTextSize(size)
pcbnew.Refresh()
print("Silkscreen updated")
