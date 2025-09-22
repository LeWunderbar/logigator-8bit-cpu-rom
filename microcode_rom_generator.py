# microcode_rom_generator.py

# Output Bit Index
CONTROL_BITS = {
    "IO": 0,
    "II": 1,
    "HLT": 2,
    "OI": 3,
    "RO": 4,
    "RI": 5,
    "MI": 6,
    "J": 7,
    "CE": 8,
    "CO": 9,
    "BI": 10,
    "SU": 11,
    "eO": 12,
    "FI": 13,
    "AO": 14,
    "AI": 15,
}

def encode(signals):
    word = 0
    for sig in signals:
        word |= (1 << CONTROL_BITS[sig])
    return word & 0xFFFF

NUM_OPCODES = 16
NUM_STEPS = 8
rom = []

MICROCODE = { # (opcode, step) -> [signals]
    # NOP (0000)
    (0, 2): [],

    # LDA (0001)
    (1, 2): ["MI", "IO"],
    (1, 3): ["RO", "AI"],

    # ADD (0010)
    (2, 2): ["MI", "IO"],
    (2, 3): ["RO", "BI"],
    (2, 4): ["eO", "AI"],

    # SUB (0011) 
    (3, 2): ["MI", "IO"],
    (3, 3): ["RO", "BI"],
    (3, 4): ["eO", "AI", "SU"],

    # STA (0100)
    (4, 2): ["MI", "IO"],
    (4, 3): ["AO", "RI"],

    # LDI (0101)
    (5, 2): ["AI", "IO"],

    # JMP (0110)
    (6, 2): ["IO", "J"],

    # JC (0111)
    (7, 2): ["IO", "J"],

    # JZ (1000)
    (8, 2): ["IO", "J"],



    # OUT (1110)
    (14, 2): ["AO", "OI"],

    # HLT (1111)
    (15, 2): ["HLT"],
}

# Precompute last execution step per instruction (exclude fetch)
LAST_STEP = {}
for opcode in range(NUM_OPCODES):
    active_steps = [step for step in range(2, NUM_STEPS) if MICROCODE.get((opcode, step))]
    if active_steps:
        LAST_STEP[opcode] = max(active_steps)
    else:
        LAST_STEP[opcode] = None

for c in range(2):         # Carry flag (A8)
    for z in range(2):     # Zero flag  (A7)
        for step in range(NUM_STEPS):    
            for opcode in range(NUM_OPCODES):  
                # fetch steps
                if step == 0:
                    signals = ["MI", "CO"]
                elif step == 1:
                    signals = ["RO", "II"]
                else:
                    signals = MICROCODE.get((opcode, step), [])

                    # Conditional logic for jumps 
                    # (CHANGE OPCODE HERE IF OPCODE FOR JZ OR JC CHANGE!)
                    if opcode == 8 and z == 0:   # JZ but Zero=0 -> no jump
                        signals = []
                    if opcode == 7 and c == 0:   # JC but Carry=0 -> no jump
                        signals = []

                # Add CE on last step of instruction
                if LAST_STEP[opcode] is not None and step == LAST_STEP[opcode]:
                    if "CE" not in signals:
                        signals.append("CE")

                word = encode(signals)
                lo = word & 0xFF
                hi = (word >> 8) & 0xFF
                rom.append(f"{lo:02X} {hi:02X}")

print(" ".join(rom))
