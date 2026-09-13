#!/usr/bin/env python3
import json
import numpy as np
from collections import defaultdict

def get_residue_plddt(data):
    """
    Calcula el pLDDT promedio por residuo a partir de atom_plddts y token_res_ids.
    """
    atom_plddts = data['atom_plddts']
    token_res_ids = data['token_res_ids']
    
    n_residues = len(token_res_ids)
    n_atoms = len(atom_plddts)
    
    print(f"Residuos: {n_residues}, Átomos: {n_atoms}")
    print(f"Ratio átomos/residuo: {n_atoms/n_residues:.2f}")
    
    # Calcular pLDDT promedio por residuo
    residue_avg_plddt = {}
    atoms_per_residue = n_atoms // n_residues
    
    print(f"Átomos por residuo (aproximado): {atoms_per_residue}")
    
    for i in range(n_residues):
        start_idx = i * atoms_per_residue
        end_idx = start_idx + atoms_per_residue
        
        if end_idx > n_atoms:
            end_idx = n_atoms
            
        atom_values = atom_plddts[start_idx:end_idx]
        avg_plddt = np.mean(atom_values)
        
        res_id = token_res_ids[i]
        residue_avg_plddt[res_id] = avg_plddt
    
    return residue_avg_plddt

def main():
    print("=== Comparación de pLDDT: WT vs Mutante (AlphaFold 3) ===\n")
    
    # Cargar datos del WT
    with open('wt/fold_bub1b_wt_full_data_0.json') as f:
        wt_data = json.load(f)
    
    # Cargar datos del mutante
    with open('mutant/fold_bub1b_n1002k_mutant_full_data_0.json') as f:
        mut_data = json.load(f)
    
    # Calcular pLDDT por residuo
    print("Procesando WT:")
    wt_plddt = get_residue_plddt(wt_data)
    print(f"Residuos procesados: {len(wt_plddt)}\n")
    
    print("Procesando Mutante:")
    mut_plddt = get_residue_plddt(mut_data)
    print(f"Residuos procesados: {len(mut_plddt)}\n")
    
    # Comparar posición 1002
    print("=" * 60)
    print("COMPARACIÓN EN POSICIÓN 1002 (p.Asn1002Lys)")
    print("=" * 60)
    
    if 1002 in wt_plddt and 1002 in mut_plddt:
        wt_val = wt_plddt[1002]
        mut_val = mut_plddt[1002]
        diff = mut_val - wt_val
        
        print(f"WT pLDDT:     {wt_val:.2f}")
        print(f"Mutante pLDDT: {mut_val:.2f}")
        print(f"Diferencia:    {diff:+.2f}")
        print()
        
        # Interpretación
        if diff > 0:
            print("✓ La mutación INCREMENTA la confianza estructural")
        elif diff < 0:
            print("✗ La mutación DECREMENTA la confianza estructural")
        else:
            print("= La mutación NO cambia la confianza estructural")
        print()
        
        # Contexto de posiciones cercanas
        print("=" * 60)
        print("CONTEXTO: Posiciones 997-1007")
        print("=" * 60)
        print(f"{'Pos':>5} {'WT':>8} {'Mut':>8} {'Δ':>8}")
        print("-" * 60)
        
        for pos in range(997, 1008):
            if pos in wt_plddt and pos in mut_plddt:
                wt_v = wt_plddt[pos]
                mut_v = mut_plddt[pos]
                d = mut_v - wt_v
                marker = " <--" if pos == 1002 else ""
                print(f"{pos:>5} {wt_v:>8.2f} {mut_v:>8.2f} {d:>+8.2f}{marker}")
        
        print()
        
        # Guardar resultados completos
        results = {
            'position_1002': {
                'wt_plddt': float(wt_val),
                'mut_plddt': float(mut_val),
                'difference': float(diff)
            },
            'context': {}
        }
        
        for pos in range(997, 1008):
            if pos in wt_plddt and pos in mut_plddt:
                results['context'][str(pos)] = {
                    'wt': float(wt_plddt[pos]),
                    'mut': float(mut_plddt[pos]),
                    'diff': float(mut_plddt[pos] - wt_plddt[pos])
                }
        
        with open('plddt_comparison_1002.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"Resultados guardados en: plddt_comparison_1002.json")
        
    else:
        print("ERROR: No se pudo encontrar la posición 1002 en los datos")
        print(f"WT tiene posiciones: {sorted(wt_plddt.keys())[:10]} ... {sorted(wt_plddt.keys())[-10:]}")
        print(f"Mut tiene posiciones: {sorted(mut_plddt.keys())[:10]} ... {sorted(mut_plddt.keys())[-10:]}")

if __name__ == "__main__":
    main()
