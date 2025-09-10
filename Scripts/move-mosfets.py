import pcbnew

board = pcbnew.GetBoard()

# Settings
top_refs = ["Q1", "Q3", "Q5"]
bottom_refs = ["Q2", "Q4", "Q6"]
spacing_y = 20.0   # Distance between Q1, Q3, Q5 in mm
offset_y = 8.55    # Distance below each top transistor in mm

def mm_to_nm(mm):
    return int(mm * 1e6)

# Get starting point from Q1 position
q1 = board.FindFootprintByReference(top_refs[0])
if q1 is None:
    raise ValueError(f"Footprint {top_refs[0]} not found")

start_y = q1.GetPosition().y

# Place Q1, Q3, Q5
for i, ref in enumerate(top_refs):
    fp = board.FindFootprintByReference(ref)
    if fp:
        new_y = start_y + mm_to_nm(i * spacing_y)
        fp.SetPosition(pcbnew.VECTOR2I(fp.GetPosition().x, new_y))

# Place Q2, Q4, Q6 below each top transistor
for i, ref in enumerate(bottom_refs):
    fp_bottom = board.FindFootprintByReference(ref)
    fp_top = board.FindFootprintByReference(top_refs[i])
    if fp_bottom and fp_top:
        new_y = fp_top.GetPosition().y + mm_to_nm(offset_y)
        fp_bottom.SetPosition(pcbnew.VECTOR2I(fp_top.GetPosition().x, new_y))

pcbnew.Refresh()
print("Done positioning footprints!")
