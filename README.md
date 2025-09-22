# Logigator 8-bit CPU ROM Generator

This repository contains Python tools for my custom **8-bit CPU** designed and built in [Logigator](https://logigator.com/).  
It provides scripts to generate ROM data for the instruction set and, later, an assembler to write programs in a custom assembly language.  

🔗 Original CPU design: [lumcuper.carrd.co](https://lumcuper.carrd.co)  

---

## 🧾 Introduction

The project currently contains two Python scripts:

1. **`microcode_rom_generator.py`** – generates the **Instruction ROM** contents, which control how each instruction executes step by step.  
2. **`assembler.py`** – *(work in progress)* will assemble custom-written programs into binary ROM data for program memory.  

The ROMs generated here are meant to be loaded into ROM chips inside the Logigator project of the CPU.  

---

## ⚙️ microcode_rom_generator.py

This script builds the **Instruction ROM** for the CPU.  
Each instruction is broken down into microinstructions (control signals), which are encoded into ROM data.  
This ROM defines how the CPU executes each instruction step by step, including automatically enabling the **Program Counter (CE)** at the final step of each instruction.  

### Instruction ROM Pinout

#### Outputs (control signals)

| Pin | Signal | Description                  |
|-----|--------|------------------------------|
| 0   | IO     | Instruction Register Out     |
| 1   | II     | Instruction Register In      |
| 2   | HLT    | Halt CPU                     |
| 3   | OI     | Output Register In           |
| 4   | RO     | RAM Out                      |
| 5   | RI     | RAM In                       |
| 6   | MI     | Memory Address Register In   |
| 7   | J      | Jump (load PC)               |
| 8   | CE     | Program Counter Enable       |
| 9   | CO     | Program Counter Out          |
| 10  | BI     | B Register In                |
| 11  | SU     | Subtract Enable              |
| 12  | eO     | ALU Out                      |
| 13  | FI     | Flags In                     |
| 14  | AO     | A Register Out               |
| 15  | AI     | A Register In                |
| 16  | SC     | Step Counter Reset           |

#### Inputs (address lines)

| Pin | Signal       |
|-----|--------------|
| A0  | Opcode Bit 1 |
| A1  | Opcode Bit 2 |
| A2  | Opcode Bit 4 |
| A3  | Opcode Bit 8 |
| A4  | Step Bit 1   |
| A5  | Step Bit 2   |
| A6  | Step Bit 4   |
| A7  | Zero Flag    |
| A8  | Carry Flag   |

---

## 🛠️ assembler.py *(placeholder)*

This script will serve as a **custom assembler** for the CPU.  
It will take in programs written in a human-readable assembly language (11 instructions supported by the CPU) and output ROM data that can be loaded into the **Program ROM**.  

### Planned Features
- Define mnemonics for all CPU instructions.  
- Translate instructions into binary machine code.  
- Export ROM data in a format that can be directly loaded into the CPU’s Program ROM.  
- Support labels and jumps.  

*(Coming soon!)*  

---

## 🚀 Roadmap

- [x] Instruction ROM generator (`microcode_rom_generator.py`)  
- [ ] Assembler for custom assembly language (`assembler.py`)  
- [ ] Example programs  
- [ ] Demo projects in Logigator  

---

## ⚡ About

This project is part of my hobby CPU design.  
The CPU was built in **Logigator** and implements 11 instructions.  
This repository makes it easier to write programs and generate the required ROM data to run them.  

🔗 My Original design: [lumcuper.carrd.co](https://lumcuper.carrd.co)
