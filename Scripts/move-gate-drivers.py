import pcbnew

board = pcbnew.GetBoard()

def mm_to_nm(mm):
    return int(mm * 1e6)

# --- Offsets for each group ---
moves = [
    # U6, U7 relative to Q4, Q6
    (("Q4", "U6"), -14.1, -0.95),
    (("Q6", "U7"), -14.1, -0.95),

    # R7, R11, R15 relative to Q2, Q4, Q6
    (("Q2", "R7"), -5.55, -4.55),
    (("Q4", "R11"), -5.55, -4.55),
    (("Q6", "R15"), -5.55, -4.55),

    # R8, R12, R16 relative to Q2, Q4, Q6
    (("Q2", "R8"), -5.55, 1.4),
    (("Q4", "R12"), -5.55, 1.4),
    (("Q6", "R16"), -5.55, 1.4),

    # C18, C23, C28 relative to Q2, Q4, Q6 at (-14.1, -11)
    (("Q2", "C18"), -14.1, -11),
    (("Q4", "C23"), -14.1, -11),
    (("Q6", "C28"), -14.1, -11),

    # C19, C24, C29 relative to Q2, Q4, Q6 at (-14.1, -8.5)
    (("Q2", "C19"), -14.1, -8.5),
    (("Q4", "C24"), -14.1, -8.5),
    (("Q6", "C29"), -14.1, -8.5),
]

# --- Apply moves ---
for (q_ref, part_ref), dx, dy in moves:
    q_fp = board.FindFootprintByReference(q_ref)
    part_fp = board.FindFootprintByReference(part_ref)

    if q_fp is None:
        print(f"Footprint {q_ref} not found, skipping")
        continue
    if part_fp is None:
        print(f"Footprint {part_ref} not found, skipping")
        continue

    q_pos = q_fp.GetPosition()
    new_x = q_pos.x + mm_to_nm(dx)
    new_y = q_pos.y + mm_to_nm(dy)

    part_fp.SetPosition(pcbnew.VECTOR2I(new_x, new_y))
    print(f"Moved {part_ref} relative to {q_ref} (dx={dx}, dy={dy})")

pcbnew.Refresh()
print("All parts moved successfully!")
