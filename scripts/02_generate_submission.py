#!/usr/bin/env python3
"""
Generate Track 1 submission CSV for MVA Hackathon 2026.
Team: Los omikos | Author: JoseVelasco22

This script generates the predictions CSV file for Track 1.
The primary finding is a compound heterozygous BUB1B configuration:
  - chr15:40209701 T>G (p.Leu737*, ClinVar PATHOGENIC)
  - chr15:40220612 T>G (p.Asn1002Lys, VUS, AlphaMissense 0.923)
"""

import csv
from pathlib import Path

def main():
    output_file = Path("submission/JoseVelasco22_exomiser-bub1b-compoundhet.csv")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    rows = [
        {
            "proband_id": "WGS_EX2312012",
            "chrom_1": "chr15",
            "pos_1": 40209701,
            "ref_1": "T",
            "alt_1": "G",
            "chrom_2": "chr15",
            "pos_2": 40220612,
            "ref_2": "T",
            "alt_2": "G",
            "epcr": 0.9819,
            "finding_type": "primary",
            "notes": "Compound heterozygous BUB1B: p.Leu737* (ClinVar ID 533901, PATHOGENIC_OR_LIKELY_PATHOGENIC, 2 stars) and p.Asn1002Lys (VUS, AlphaMissense 0.923). Mosaic variegated aneuploidy syndrome 1 (OMIM:257300). Exomiser combined score 0.9819, rank 1 in both 51-gene panel and genome-wide coding analysis. Phase inferred by functional parsimony."
        }
    ]

    fieldnames = ["proband_id", "chrom_1", "pos_1", "ref_1", "alt_1",
                  "chrom_2", "pos_2", "ref_2", "alt_2", "epcr", "finding_type", "notes"]

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Submission CSV generated: {output_file}")
    print(f"Rows: {len(rows)}")

if __name__ == "__main__":
    main()
