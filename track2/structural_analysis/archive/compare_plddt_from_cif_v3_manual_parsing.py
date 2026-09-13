#!/usr/bin/env python3
import numpy as np
from collections import defaultdict

def extract_plddt_from_cif(cif_file):
    """
    Extrae pLDDT por residuo desde un archivo mmCIF.
    El pLDDT está en la columna B-factor de las líneas ATOM.
    """
    residue_plddts = defaultdict(list)
    
    with open(cif_file, 'r') as f:
        in_atom_site = False
        for line in f:
            # Detectar inicio de sección ATOM
            if line.startswith('loop_'):
                continue
            if line.startswith('_atom_site.'):
                in_atom_site = True
                continue
            
            # Procesar líneas ATOM
            if in_atom_site and line.startswith('ATOM'):
                # Formato mmCIF: campos separados por espacios
                # El formato exacto varía, pero típicamente:
                # ATOM serial type_symbol label_atom_id label_comp_id label_asym_id label_seq_id Cartn_x Cartn_y Cartn_z occupancy B_iso_or_equiv
                parts = line.split()
                if len(parts) >= 18:
                    try:
                        # label_seq_id es típicamente el campo 8 (índice 7 en 0-based)
                        residue_num = int(parts[8])
                        # B_iso_or_equiv es típicamente el último campo
                        b_factor = float(parts[-1])
                        residue_plddts[residue_num].append(b_factor)
                    except (ValueError, IndexError):
                        continue
    
    # Calcular promedio por residuo
    avg_plddt = {}
    for res_num, values in residue_plddts.items():
        avg_plddt[res_num] = np.mean(values)
    
    return avg_plddt

def analyze_condition(model_files, condition_name):
    """Analiza todos los modelos de una condición."""
    print(f"\n{'='*60}")
    print(f"Análisis de {condition_name}")
    print(f"{'='*60}")
    
    all_plddt_1002 = []
    all_plddt_by_position = defaultdict(list)
    
    for i, cif_file in enumerate(model_files):
        print(f"\nProcesando modelo {i}: {cif_file}")
        plddt_map = extract_plddt_from_cif(cif_file)
        
        # Extraer pLDDT en posición 1002
        plddt_1002 = plddt_map.get(1002, None)
        if plddt_1002 is not None:
            all_plddt_1002.append(plddt_1002)
            print(f"  pLDDT en posición 1002: {plddt_1002:.2f}")
        
        # Guardar pLDDT de posiciones cercanas (997-1007)
        for pos in range(997, 1008):
            if pos in plddt_map:
                all_plddt_by_position[pos].append(plddt_map[pos])
    
    # Estadísticas para posición 1002
    if all_plddt_1002:
        print(f"\nEstadísticas para posición 1002:")
        print(f"  Media: {np.mean(all_plddt_1002):.2f}")
        print(f"  SD: {np.std(all_plddt_1002):.2f}")
        print(f"  Rango: {np.min(all_plddt_1002):.2f} - {np.max(all_plddt_1002):.2f}")
    
    # Estadísticas para posiciones cercanas
    print(f"\nContexto (posiciones 997-1007):")
    print(f"{'Pos':>5} {'Media':>8} {'SD':>6} {'Min':>8} {'Max':>8}")
    print("-" * 40)
    for pos in range(997, 1008):
        if pos in all_plddt_by_position:
            values = all_plddt_by_position[pos]
            marker = " <--" if pos == 1002 else ""
            print(f"{pos:>5} {np.mean(values):>8.2f} {np.std(values):>6.2f} "
                  f"{np.min(values):>8.2f} {np.max(values):>8.2f}{marker}")
    
    return all_plddt_1002, all_plddt_by_position

# Ejecutar análisis
import glob

wt_files = sorted(glob.glob('wt/fold_bub1b_wt_model_*.cif'))
mut_files = sorted(glob.glob('mutant/fold_bub1b_n1002k_mutant_model_*.cif'))

print(f"Archivos WT encontrados: {len(wt_files)}")
print(f"Archivos mutante encontrados: {len(mut_files)}")

wt_1002, wt_by_pos = analyze_condition(wt_files, "Wild-Type (WT)")
mut_1002, mut_by_pos = analyze_condition(mut_files, "Mutante N1002K")

# Comparación final
print(f"\n{'='*60}")
print(f"COMPARACIÓN FINAL")
print(f"{'='*60}")

if wt_1002 and mut_1002:
    wt_mean = np.mean(wt_1002)
    wt_std = np.std(wt_1002)
    mut_mean = np.mean(mut_1002)
    mut_std = np.std(mut_1002)
    delta = mut_mean - wt_mean
    
    print(f"\nWT (n={len(wt_1002)}):")
    print(f"  Media: {wt_mean:.2f} ± {wt_std:.2f} (SD)")
    
    print(f"\nMutante (n={len(mut_1002)}):")
    print(f"  Media: {mut_mean:.2f} ± {mut_std:.2f} (SD)")
    
    print(f"\nDelta (Mut - WT): {delta:+.2f}")
    
    # Interpretación
    print(f"\n{'='*60}")
    print(f"INTERPRETACIÓN")
    print(f"{'='*60}")
    
    if abs(delta) < 2:
        print("✓ Delta pequeño (<2 puntos)")
        print("  La mutación no tiene efecto significativo en la confianza estructural")
    elif abs(delta) < 5:
        print("⚠ Delta moderado (2-5 puntos)")
        print("  Posible efecto leve de la mutación")
    else:
        print("✗ Delta significativo (>5 puntos)")
        if delta < 0:
            print("  La mutación causa desestabilización estructural")
        else:
            print("  La mutación aumenta la confianza (efecto inesperado)")
    
    # Verificar si el delta excede la variabilidad intra-seed
    max_std = max(wt_std, mut_std)
    if abs(delta) > 2 * max_std:
        print(f"\n✓ El delta ({abs(delta):.2f}) EXCEDE 2× la SD intra-seed ({max_std:.2f})")
        print("  Resultado estadísticamente robusto")
    else:
        print(f"\n⚠ El delta ({abs(delta):.2f}) NO excede 2× la SD intra-seed ({max_std:.2f})")
        print("  Resultado marginal, difícil de distinguir del ruido del modelo")

