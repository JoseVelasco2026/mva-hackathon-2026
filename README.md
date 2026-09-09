# MVA Hackathon 2026 — Track 1: Variant Identification

**Team:** Los omikos  
**Author:** JoseVelasco22  
**Submission date:** 2026-09-08

## Summary

We identified a **compound heterozygous** configuration in **BUB1B** (OMIM: 602789) as the causal basis of **Mosaic Variegated Aneuploidy syndrome 1** (OMIM: 257300) in proband `PROBAND01`.

| Field | Value |
|-------|-------|
| **Gene** | BUB1B |
| **Variant 1** | chr15:40,209,701 T>G — p.Leu737* (nonsense, ClinVar PATHOGENIC, 2 stars) |
| **Variant 2** | chr15:40,220,612 T>G — p.Asn1002Lys (missense, VUS, AlphaMissense 0.923) |
| **Inheritance** | Autosomal recessive, compound heterozygous (trans, inferred by functional parsimony) |
| **EPCR** | 0.9819 |
| **Finding type** | primary |

## Approach

### Orthogonal validation strategy

We ran Exomiser v14.0.0 under three independent configurations to verify robustness:

| Configuration | Genes analyzed | BUB1B rank | Combined score |
|---|---|---|---|
| Targeted panel (22 MVA genes) | 22 | 1 | 0.9819 |
| Expanded panel (51 SAC/DNA-repair genes) | 51 | 1 | 0.9819 |
| Genome-wide (coding + splice only) | ~20,000 | 1 | 0.9819 |

BUB1B maintained **identical score 0.9819** across all three configurations, demonstrating the finding does not depend on gene-set definition.

### Forensic validation of limitations

We explicitly interrogated and closed four methodological gaps:

1. **Structural variant exclusion:** Mean depth of coverage in the BUB1B region (chr15:40.1–40.3 Mb) was 43.2×, virtually identical to a control region on chr15 (43.3×), grossly consistent with diploid copy number across the region. However, this coarse mean-depth comparison over a ~200 kb window lacks resolution to detect smaller CNVs; a dedicated SV/CNV caller would be needed to formally exclude these.
2. **False-positive dismissal in the MHC:** HLA-DRB1 (chr6) emerged as rank 2 in the genome-wide run with score 0.9624. We rejected it as an artifact of extreme polymorphism at the MHC locus, noting its pheno score (0.7067) was substantially below BUB1B's (0.8134).
3. **Phase inference via functional parsimony:** The FORMAT field of the two BUB1B variants contains no phasing tags, though PGT/PID tags are present at other nearby sites in the region (the caller attempted read-backed phasing elsewhere, but not here). At 10.9 kb apart, the two variants exceed short-read fragment size and were emitted unphased. We resolved phase by Mendelian parsimony: under the *cis* configuration one allele would remain wild-type (inconsistent with severe MVA). Only the *trans* configuration is compatible.
4. **Promoter/UTR exclusion:** No PASS variants were found in the corrected BUB1B promoter (chr15:40,159,000–40,162,000).

## Repository structure

```text
mva-hackathon-2026/
├── README.md
├── configs/                     # Exomiser configurations
│   ├── application.properties
│   ├── exomiser_job_panel22.yml
│   ├── exomiser_job_panel51.yml
│   ├── exomiser_job_genomewide.yml
│   └── phenopacket_original.yml
├── scripts/                     # Reproducible analysis scripts
│   ├── 01_forensic_validation.sh
│   ├── 02_generate_submission.py
│   └── 03_generate_methods_excel.py
├── submission/                  # Hackathon submission files
│   ├── JoseVelasco22_exomiser-bub1b-compoundhet.csv
│   ├── JoseVelasco22_track1_report.md
│   └── JoseVelasco22_track1_methods.xlsx
└── results/                     # Exomiser output (TSV files)
    ├── mva_patient_01_panel.genes.tsv
    ├── mva_patient_01_panel.variants.tsv
    ├── mva_patient_01_expanded.genes.tsv
    ├── mva_patient_01_expanded.variants.tsv
    ├── mva_patient_01_nopanel.genes.tsv
    └── mva_patient_01_nopanel.variants.tsv
```

## How to reproduce

### Prerequisites
- Exomiser v14.0.0
- Java 21
- Exomiser reference data (2406_hg38, 2406_phenotype)
- Python 3.8+ with `openpyxl`

### Run analysis

```bash
# 1. Copy application.properties to Exomiser directory
cp configs/application.properties /path/to/exomiser-cli-14.0.0/

# 2. Run the three orthogonal Exomiser configurations
java -Xmx6g -jar exomiser-cli-14.0.0.jar --job configs/exomiser_job_panel22.yml
java -Xmx6g -jar exomiser-cli-14.0.0.jar --job configs/exomiser_job_panel51.yml
java -Xmx6g -jar exomiser-cli-14.0.0.jar --job configs/exomiser_job_genomewide.yml

# 3. Run forensic validation
bash scripts/01_forensic_validation.sh

# 4. Regenerate submission files (optional)
python scripts/02_generate_submission.py
python scripts/03_generate_methods_excel.py
```

## AI/LLM usage

- **Providers:** Alibaba Cloud (Qwen 3 Max) + Anthropic (Claude)
- **Plan/tier:** Commercial
- **Data handling:** No training on customer content
- **Role:** Methodological reasoning assistants, not automated variant callers

All variant calls were produced by Exomiser v14.0.0 and validated against raw VCF and ClinVar evidence by the human analyst.

## References

- Hanks S et al. (2004). *Nat Genet* 36:1159–1161. BUB1B mutations in MVA.
- OMIM:257300 — Mosaic Variegated Aneuploidy Syndrome 1
- OMIM:602789 — BUB1B gene
- ClinVar Variation ID 533901
- Exomiser v14.0.0 documentation

## License

This repository will be made public after the hackathon ends, as required by the competition rules.
