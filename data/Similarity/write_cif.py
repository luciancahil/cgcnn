#!/usr/bin/env python3
"""
batch_traj2cif.py — Convert all ASE .traj files in the current directory to .cif

Usage:
  python batch_traj2cif.py
"""

import os
from ase.io import read, write

def main():
    cwd = os.getcwd()
    traj_files = [f for f in os.listdir(cwd) if f.endswith(".traj")]

    if not traj_files:
        print("No .traj files found in the current directory.")
        return

    for traj_file in traj_files:
        try:
            # Read last frame
            atoms = read(traj_file, index=-1)
            cif_file = os.path.splitext(traj_file)[0] + ".cif"

            write(cif_file, atoms, format="cif", wrap=True)
            print(f"Converted {traj_file} → {cif_file}")
        except Exception as e:
            print(f"Error converting {traj_file}: {e}")

if __name__ == "__main__":
    main()
