#!/usr/bin/env python3
from Bio.PDB.MMCIFParser import MMCIFParser
import numpy as np
import glob

def get_ca_plddt(cif_file):
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure('model', cif_file)
    plddt_by_res = {}
    for model in structure:
        for chain in model:
            for residue in chain:
                if 'CA' in residue:
                    plddt_by_res[residue.id[1]] = residue['CA'].get_bfactor()
    return plddt_by_res

def main():
    positions = list(range(997, 1008))
    wt_files = sorted(glob.glob('wt/fold_bub1b_wt_model_*.cif'))
    mut_files = sorted(glob.glob('mutant/fold_bub1b_n1002k_mutant_model_*.cif'))

    wt_vals = {p: [] for p in positions}
    mut_vals = {p: [] for p in positions}

    for f in wt_files:
        plddt = get_ca_plddt(f)
        for p in positions:
            if p in plddt:
                wt_vals[p].append(plddt[p])

    for f in mut_files:
        plddt = get_ca_plddt(f)
        for p in positions:
            if p in plddt:
                mut_vals[p].append(plddt[p])

    print(f"{'Pos':>5} {'WT mean':>10} {'WT SD':>8} {'Mut mean':>10} {'Mut SD':>8} {'Delta':>8}")
    for p in positions:
        wt_arr, mut_arr = np.array(wt_vals[p]), np.array(mut_vals[p])
        marker = " <--" if p == 1002 else ""
        print(f"{p:>5} {wt_arr.mean():>10.2f} {wt_arr.std():>8.2f} {mut_arr.mean():>10.2f} {mut_arr.std():>8.2f} {mut_arr.mean()-wt_arr.mean():>+8.2f}{marker}")

if __name__ == "__main__":
    main()
