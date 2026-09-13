#!/usr/bin/env python3
import json
import numpy as np
from collections import defaultdict

# Tabla de átomos pesados (no-H) por aminoácido en estructuras PDB estándar
# (N, CA, C, O + cadena lateral)
HEAVY_ATOMS_PER_AA = {
    'A': 5,   # Ala: N,CA,C,O,CB
    'R': 11,  # Arg: N,CA,C,O,CB,CG,CD,NE,CZ,NH1,NH2
    'N': 8,   # Asn: N,CA,C,O,CB,CG,OD1,ND2
    'D': 8,   # Asp: N,CA,C,O,CB,CG,OD1,OD2
    'C': 6,   # Cys: N,CA,C,O,CB,SG
    'E': 9,   # Glu: N,CA,C,O,CB,CG,CD,OE1,OE2
    'Q': 9,   # Gln: N,CA,C,O,CB,CG,CD,OE1,NE2
    'G': 4,   # Gly: N,CA,C,O
    'H': 10,  # His: N,CA,C,O,CB,CG,ND1,CD2,CE1,NE2
    'I': 8,   # Ile: N,CA,C,O,CB,CG1,CG2,CD1
    'L': 8,   # Leu: N,CA,C,O,CB,CG,CD1,CD2
    'K': 9,   # Lys: N,CA,C,O,CB,CG,CD,CE,NZ
    'M': 8,   # Met: N,CA,C,O,CB,CG,SD,CE
    'F': 11,  # Phe: N,CA,C,O,CB,CG,CD1,CD2,CE1,CE2,CZ
    'P': 7,   # Pro: N,CA,C,O,CB,CG,CD
    'S': 6,   # Ser: N,CA,C,O,CB,OG
    'T': 7,   # Thr: N,CA,C,O,CB,OG1,CG2
    'W': 14,  # Trp: N,CA,C,O,CB,CG,CD1,CD2,NE1,CE2,CE3,CZ2,CZ3,CH2
    'Y': 12,  # Tyr: N,CA,C,O,CB,CG,CD1,CD2,CE1,CE2,CZ,OH
    'V': 7,   # Val: N,CA,C,O,CB,CG1,CG2
}

def get_plddt_by_residue_correct(full_data_file):
    """Extrae pLDDT por residuo usando el conteo real de átomos por aminoácido."""
    with open(full_data_file) as f:
        data = json.load(f)
    
    atom_plddts = data['atom_plddts']
    token_res_ids = data['token_res_ids']
    
    # Necesitamos la secuencia para saber qué aminoácido hay en cada posición
    # AlphaFold3 no la incluye en full_data, así que la cargamos del FASTA
    return atom_plddts, token_res_ids

def compare_with_correct_mapping(wt_file, mut_file, wt_fasta, mut_fasta, target_pos=1002):
    """Compara pLDDT usando mapeo correcto de átomos a residuos."""
    
    # Cargar secuencias
    with open(wt_fasta) as f:
        wt_seq = ''.join(line.strip() for line in f if not line.startswith('>'))
    
    with open(mut_fasta) as f:
        mut_seq = ''.join(line.strip() for line in f if not line.startswith('>'))
    
    # Cargar datos
    with open(wt_file) as f:
        wt_data = json.load(f)
    with open(mut_file) as f:
        mut_data = json.load(f)
    
    wt_atom_plddts = wt_data['atom_plddts']
    mut_atom_plddts = mut_data['atom_plddts']
    
    print(f"Secuencia WT: {len(wt_seq)} residuos, {len(wt_atom_plddts)} átomos")
    print(f"Secuencia Mut: {len(mut_seq)} residuos, {len(mut_atom_plddts)} átomos")
    print(f"Diferencia de átomos: {len(mut_atom_plddts) - len(wt_atom_plddts)}")
    
    # Verificar que el cambio Asn→Lys agrega exactamente 1 átomo
    wt_aa = wt_seq[target_pos - 1]
    mut_aa = mut_seq[target_pos - 1]
    expected_diff = HEAVY_ATOMS_PER_AA[mut_aa] - HEAVY_ATOMS_PER_AA[wt_aa]
    actual_diff = len(mut_atom_plddts) - len(wt_atom_plddts)
    
    print(f"\nCambio en posición {target_pos}: {wt_aa} → {mut_aa}")
    print(f"Átomos esperados: {HEAVY_ATOMS_PER_AA[wt_aa]} → {HEAVY_ATOMS_PER_AA[mut_aa]} (diff: {expected_diff})")
    print(f"Diferencia real de átomos: {actual_diff}")
    print(f"Consistencia: {'✓' if expected_diff == actual_diff else '✗'}")
    
    # Construir mapeo correcto de átomos a residuos
    def build_atom_to_residue_map(seq, atom_plddts):
        """Construye mapeo de índice de átomo a residuo usando conteo real."""
        residue_plddts = {}
        atom_idx = 0
        
        for res_idx, aa in enumerate(seq):
            n_atoms = HEAVY_ATOMS_PER_AA.get(aa, 8)  # Default 8 si no está en la tabla
            
            # Extraer pLDDT de los átomos de este residuo
            start = atom_idx
            end = min(atom_idx + n_atoms, len(atom_plddts))
            
            if start < len(atom_plddts):
                atom_values = atom_plddts[start:end]
                avg_plddt = np.mean(atom_values)
                residue_plddts[res_idx + 1] = avg_plddt  # 1-based indexing
            
            atom_idx += n_atoms
        
        return residue_plddts
    
    print("\nConstruyendo mapeo correcto de átomos a residuos...")
    wt_plddt_map = build_atom_to_residue_map(wt_seq, wt_atom_plddts)
    mut_plddt_map = build_atom_to_residue_map(mut_seq, mut_atom_plddts)
    
    print(f"Residuos mapeados - WT: {len(wt_plddt_map)}, Mut: {len(mut_plddt_map)}")
    
    # Comparar posición objetivo
    print(f"\n=== COMPARACIÓN EN POSICIÓN {target_pos} ===")
    wt_val = wt_plddt_map.get(target_pos, None)
    mut_val = mut_plddt_map.get(target_pos, None)
    
    if wt_val and mut_val:
        delta = mut_val - wt_val
        print(f"WT pLDDT: {wt_val:.2f}")
        print(f"Mutante pLDDT: {mut_val:.2f}")
        print(f"Delta: {delta:+.2f}")
        
        # Verificar posiciones cercanas
        print(f"\n=== CONTEXTO: Posiciones {target_pos-5} a {target_pos+5} ===")
        print(f"{'Pos':>5} {'WT':>8} {'Mut':>8} {'Δ':>8}")
        print("-" * 40)
        
        for pos in range(target_pos - 5, target_pos + 6):
            wt_p = wt_plddt_map.get(pos, None)
            mut_p = mut_plddt_map.get(pos, None)
            if wt_p and mut_p:
                d = mut_p - wt_p
                marker = " <--" if pos == target_pos else ""
                print(f"{pos:>5} {wt_p:>8.2f} {mut_p:>8.2f} {d:>+8.2f}{marker}")
        
        # Interpretación
        print(f"\n=== INTERPRETACIÓN ===")
        if abs(delta) < 2:
            print("Delta pequeño (<2 puntos). Diferencia probablemente dentro del ruido del modelo.")
        elif delta < 0:
            print(f"Desestabilización local de {abs(delta):.2f} puntos en la posición de la mutación.")
        else:
            print(f"Efecto inesperado: aumento de {delta:.2f} puntos en la posición de la mutación.")
        
        # Verificar si hay cascada real o es artefacto
        deltas_cercanos = []
        for pos in [target_pos + 3, target_pos + 4, target_pos + 5]:
            wt_p = wt_plddt_map.get(pos, None)
            mut_p = mut_plddt_map.get(pos, None)
            if wt_p and mut_p:
                deltas_cercanos.append(mut_p - wt_p)
        
        if deltas_cercanos and max(abs(d) for d in deltas_cercanos) > abs(delta) * 1.5:
            print("\n⚠️ ADVERTENCIA: Los deltas en posiciones cercanas son MAYORES que en la mutación.")
            print("   Esto sugiere un posible artefacto de mapeo o efectos globales del modelo.")
            print("   NO interpretar como 'cascada alostérica' sin validación adicional.")
        else:
            print("\n✓ Los deltas en posiciones cercanas son consistentes o menores.")
            print("  El efecto parece localizado a la posición de la mutación.")
        
        return {
            'position': target_pos,
            'wt_plddt': float(wt_val),
            'mut_plddt': float(mut_val),
            'delta': float(delta)
        }
    else:
        print(f"ERROR: No se encontró la posición {target_pos} en los datos")
        return None

if __name__ == "__main__":
    import sys
    
    print("=== COMPARACIÓN CORREGIDA DE pLDDT ===\n")
    
    results = compare_with_correct_mapping(
        wt_file='wt/fold_bub1b_wt_full_data_0.json',
        mut_file='mutant/fold_bub1b_n1002k_mutant_full_data_0.json',
        wt_fasta='../input/bub1b_wt.fasta',
        mut_fasta='../input/bub1b_n1002k.fasta',
        target_pos=1002
    )
    
    if results:
        with open('plddt_comparison_1002_corrected.json', 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResultados guardados en: plddt_comparison_1002_corrected.json")

