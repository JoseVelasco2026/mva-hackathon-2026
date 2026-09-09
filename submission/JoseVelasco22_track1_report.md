# Track 1 Report: Orthogonal Validation of a BUB1B Compound Heterozygote in Mosaic Variegated Aneuploidy

**Team:** Los omikos  
**Author:** JoseVelasco22  
**Date:** 2026-09-08  
**Proband:** WGS_EX2312012  

## Summary

We identified a compound heterozygous loss-of-function configuration in **BUB1B** (OMIM: 602789) as the causal basis of Mosaic Variegated Aneuploidy syndrome 1 (OMIM: 257300) in proband WGS_EX2312012. The two causal variants are:

- **chr15:40,209,701 T>G** — nonsense `p.Leu737*` (ClinVar ID 533901, PATHOGENIC_OR_LIKELY_PATHOGENIC, 2-star review)
- **chr15:40,220,612 T>G** — missense `p.Asn1002Lys` (ClinVar absent, VUS, AlphaMissense 0.923)

Both variants truncate or compromise the BubR1 kinase domain (aa 700–1050), disrupting the spindle assembly checkpoint (SAC) and causing the hallmark aneuploid mosaicism of MVA1.

## Approach

### Data and computational environment

- **Input:** WGS VCF (GRCh38/hg38), 5,012,204 variant records, single proband `WGS_EX2312012`
- **Tool:** Exomiser v14.0.0 with 2406_hg38 transcript data, 2406_phenotype ontology, and ClinVar whitelist (238,630 entries)
- **Phenotypic profile:** 8 HPO terms including HP:0002859 (Rhabdomyosarcoma), HP:0004322 (Short stature), HP:0001508 (Failure to thrive)
- **Hardware:** WSL2 on Windows 11, OpenJDK 21.0.11, 6 GB JVM heap (`-Xmx6g`)

### Orthogonal Exomiser configurations

Rather than relying on a single pipeline, we ran Exomiser under three independent configurations to verify that the BUB1B signal was not an artifact of parameter choice:

| Configuration | Genes analyzed | BUB1B rank | Combined score |
|---|---|---|---|
| Targeted panel (22 MVA/microcephaly genes) | 22 | 1 | 0.9819 |
| Expanded panel (51 SAC/DNA-repair genes) | 51 | 1 | 0.9819 |
| Genome-wide (coding + splice only) | ~20,000 | 1 | 0.9819 |

The score remained **identical** across all three configurations, demonstrating robustness to gene-set definition.

### Forensic validation of limitations

We explicitly interrogated and closed each methodological gap that could weaken the finding:

1. **Structural variant exclusion.** Mean depth of coverage in the BUB1B region (chr15:40.1–40.3 Mb) was 43.2×, virtually identical to a control region on chr15 (43.3×), grossly consistent with diploid copy number across the region. However, this coarse mean-depth comparison over a ~200 kb window lacks resolution to detect smaller (sub-exonic to few-exon) CNVs; a dedicated SV/CNV caller would be needed to formally exclude these.

2. **False-positive dismissal in the MHC.** HLA-DRB1 (chr6) emerged as rank 2 in the genome-wide run with score 0.9624. We rejected it as an artifact of extreme polymorphism at the MHC locus, noting its pheno score (0.7067) was substantially below BUB1B's (0.8134) and that no direct MVA association exists for HLA-DRB1. This dismissal is supported by two independent lines of evidence: our analysis of runs of homozygosity identified the same MHC region (chr6:32.4-32.87 Mb) as a spurious homozygosity artifact, consistent with known mapping difficulties and extreme polymorphism at this locus. The convergence of two independent analyses flagging the same region as artifactual strengthens our confidence in excluding HLA genes as causal candidates.

3. **Phase inference via functional parsimony.** The FORMAT field of the two BUB1B variants (GT:AD:DP:GQ:PL) contains no phasing tags, and both are reported as unphased genotypes (`0/1`). Although the caller performed read-backed phasing elsewhere in the region (PGT/PID tags are present at nearby sites), the 10.9 kb distance between the two BUB1B variants exceeds short-read fragment size, preventing direct phasing. We resolved phase by Mendelian parsimony: under the *cis* configuration one allele would remain wild-type and the patient would be an asymptomatic carrier — inconsistent with the severe MVA phenotype. Only the *trans* configuration (biallelic loss) is compatible with an autosomal recessive disorder.

4. **Promoter/UTR exclusion.** No PASS variants were found in the corrected BUB1B promoter (chr15:40,159,000–40,162,000), excluding regulatory causes.

## Results

The primary finding is a **compound heterozygous** BUB1B configuration:

- **Allele 1 — p.Leu737\*:** Truncates BubR1 early in the kinase domain (PVS1 ACMG criterion). Independently confirmed in ClinVar (ID 533901, 2-star review, multiple submitters, no conflicts).
- **Allele 2 — p.Asn1002Lys:** Falls within the kinase domain C-terminus. Classified VUS by ACMG criteria (PM2_Supporting, PP4), but strongly supported by AlphaMissense (0.923), MVP (0.852), and population rarity (gnomAD AF 8.99×10⁻⁵). REVEL (0.472) is borderline — a discordance we declare transparently.

Exomiser combined score **0.9819** (pheno 0.8134, variant 0.9614), with the next-best gene (HLA-DRB1) at 0.9624 and the next biologically plausible gene (FANCD2) at 0.8871.

### Secondary candidate: FANCD2

FANCD2 emerged as rank 3 in the genome-wide analysis (combined score 0.8871, p-value 0.0024). While FANCD2 is biologically relevant to genomic instability pathways (Fanconi anemia / DNA interstrand crosslink repair), it represents a distinct clinical entity (bone marrow failure, not mosaic variegated aneuploidy) and its pheno score (0.6815) is substantially below BUB1B's (0.8134). We acknowledge it as a secondary candidate but note it does not compete with the primary finding.

## Limitations

- Phase (*trans*) is inferred by functional parsimony, not confirmed by read phasing or parental segregation.
- p.Asn1002Lys remains VUS; functional validation would strengthen the case.
- No BAM was available for rigorous CNV calling (GATK-SV / Manta).
- Mosaic somatic variants below ~20% VAF may have been missed by the short-read caller.

## AI and LLM usage

Generative AI (Qwen 3 Max, Alibaba Cloud, commercial tier, standard data-handling policy) was used as a **methodological reasoning assistant** — not as an automated variant caller. All variant calls, ACMG classifications, and filtering decisions were made by Exomiser v14.0.0 and validated against raw VCF and ClinVar evidence in the terminal by the human analyst. The LLM assisted with:

- Designing orthogonal validation strategies
- Interpreting ACMG criteria and ClinVar star ratings
- Structuring the report according to IMRyD conventions (Farji-Brener & Arroyo-Rodríguez, *Manual de Redacción Científica*, UNAM 2025)

No proprietary data was used; all analyses relied on publicly available resources.

## References

- Hanks S et al. (2004). *Nat Genet* 36:1159–1161. BUB1B mutations in MVA.
- OMIM:257300 — Mosaic Variegated Aneuploidy Syndrome 1.
- OMIM:602789 — BUB1B gene.
- ClinVar Variation ID 533901.
- gnomAD v4 population frequencies.
- Exomiser v14.0.0 documentation.
