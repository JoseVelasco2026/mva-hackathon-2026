# Drug Repurposing Candidates for Mosaic Variegated Aneuploidy Syndrome 1: A Mechanism-Driven Analysis

**Team:** Los omikos
**Author:** JoseVelasco22
**Date:** 2026-09-14

---

## Abstract

Mosaic Variegated Aneuploidy syndrome 1 (MVA1, OMIM:257300) is an ultra-rare chromosomal instability disorder caused by biallelic loss-of-function mutations in *BUB1B* (OMIM:602860), encoding the spindle assembly checkpoint (SAC) protein BubR1. We identified a compound heterozygous configuration (p.Leu737* nonsense + p.Asn1002Lys missense) in proband PROBAND01 presenting with rhabdomyosarcoma, microcephaly, and failure to thrive. Through triangulation of three independent literature searches (Consensus, LeapSpace, OpenEvidence), we propose a tiered drug repurposing strategy aligned with the "market-approved medications" criterion. **Primary candidate**: Pimitespib/TAS-116 (HSP90 inhibitor, approved in Japan 2022 for refractory GIST), best mechanistic match for aneuploidy-induced proteotoxic stress. **Secondary candidate**: Dasatinib (FDA-approved tyrosine kinase inhibitor), component of senolytic combination therapy. **Forward-looking candidates**: Adavosertib (WEE1 inhibitor, discontinued development) and Sovilnesib (KIF18A inhibitor, phase I trials), included for mechanistic relevance but explicitly declared as not meeting regulatory approval criteria. Structural characterization via AlphaFold 3 comparative modeling (WT pLDDT 92.71 vs. mutant 89.84 at position 1002, with C-terminal cascading destabilization) supports loss-of-function through scaffolding disruption rather than catalytic impairment, consistent with BubR1's pseudokinase status. Critical evidence gaps include zero direct testing in BUB1B-deficient models and absence of pediatric MVA-specific safety data.

---

## 1. Introduction

### 1.1 Disease Context

Mosaic Variegated Aneuploidy syndrome 1 (MVA1) is characterized by constitutional chromosomal instability (CIN), mosaic aneuploidy, and predisposition to embryonal tumors including rhabdomyosarcoma, Wilms tumor, and leukemia [[1]]. The disorder results from biallelic loss-of-function mutations in *BUB1B* (OMIM:602860), encoding BubR1 (BUB1-related kinase 1), a core component of the spindle assembly checkpoint (SAC) that ensures accurate chromosome segregation during mitosis [[2]].

### 1.2 Mechanism of BubR1 Loss-of-Function

BubR1 functions as a **pseudokinase scaffold protein** rather than an active enzyme. Two independent lines of evidence support this characterization:

1. **Genetic/functional evidence**: Suijkerbuijk et al. (2012) demonstrated that while human BubR1 retains the catalytic triad, "putative catalysis by human BUBR1 is not essential" for SAC function [[3]].
2. **Biochemical evidence**: Breit et al. (2015) resolved the crystal structure of the Bub1 kinase domain (PDB 5DMZ) and, in the same comparative study, biochemically characterized the homologous BubR1 domain, finding that "BubR1 kinase domain binds nucleotides but is unable to deliver catalytic activity in vitro" [[4]].

This pseudokinase status has critical implications for variant interpretation: mutations in the kinase domain (residues 700-1050) likely disrupt **protein-protein interactions** (with BUB3, CDC20, APC/C) or **structural stability** rather than catalytic function.

### 1.3 Rationale for Drug Repurposing

No disease-specific therapy exists for MVA1. Current management follows standard pediatric oncology protocols (COG/EpSSG) for associated malignancies. Drug repurposing offers a viable path because:
- De novo drug development for ultra-rare disorders (<200 cases worldwide) is economically unfeasible
- Mechanism-based targeting of downstream consequences (proteotoxic stress, replication stress, senescence) is pharmacologically tractable
- Approved medications have established safety profiles, accelerating compassionate-use pathways

### 1.4 Scope Declaration

This analysis explicitly targets **market-approved medications** per Track 2 criteria. Candidates are tiered by regulatory status and mechanistic alignment, with investigational agents clearly labeled as such.

---

## 2. Methods

### 2.1 Literature Search Strategy

Three independent deep-search tools were employed to ensure comprehensive coverage and minimize selection bias:

**Consensus Deep Search** (2026-09-08):
- Query: "HSP90 inhibitors or WEE1 inhibitors aneuploidy proteotoxic stress spindle assembly checkpoint"
- Scope: Consensus operates on an indexed corpus of >220 million papers (Semantic Scholar + PubMed + other sources). For this specific query, 3.4M papers were retrieved through 19 searches, of which 100 were included in the final synthesis after relevance filtering
- Timeframe: 2010-2026
- Focus: Mechanistic alignment and preclinical evidence

**LeapSpace Deep Research** (2026-09-08):
- Query: "BUB1B loss-of-function mosaic variegated aneuploidy: which repurposed drugs target aneuploidy-induced proteotoxic stress?"
- Scope: Comprehensive evaluation of HSP90, WEE1, IGF-1R inhibitors, and senolytics
- Evidence grading: Actionability, pediatric feasibility, toxicity profile

**OpenEvidence Clinical Synthesis** (2026-09-08):
- Query: "Drug repurposing candidates for chromosomal instability syndromes like MVA1/BUB1B-related disease"
- Scope: Clinical evidence prioritization, regulatory status, safety profiles
- Unique contribution: KIF18A inhibitors identified (not searched by Consensus/LeapSpace due to scope design)

### 2.2 Scope Limitations (Explicit Declaration)

**Important methodological note**: KIF18A inhibitors (sovilnesib, VLS-1488) were only evaluated by OpenEvidence because the search queries for Consensus and LeapSpace explicitly enumerated four drug classes (HSP90, WEE1, IGF-1R, senolytics). This is not a divergence of evidence but a difference in search scope. KIF18A inhibitors are included in the "forward-looking" tier based on OpenEvidence findings.

**Note on search funnel metrics**: Consensus reports three distinct metrics at different stages of the search funnel: >220M papers represent the total indexed corpus available to the tool; 3.4M papers were retrieved for this specific query through 19 searches; 100 papers were included in the final synthesis. These are not contradictory numbers but sequential stages of the retrieval process.

### 2.3 Structural Analysis

Structural characterization of the p.Asn1002Lys variant was performed using AlphaFold 3 Server and AlphaFold DB:
- **Wild-type reference**: AlphaFold DB entry O60566 (BUB1B human, model v6), downloaded directly from the EBI API
- **Comparative modeling**: AlphaFold 3 Server predictions for both WT and p.Asn1002Lys mutant sequences
- **Confidence assessment**: pLDDT scores extracted from full_data JSON files, averaged per residue from atomic-level values
- **Validation**: No experimental human BUB1B pseudokinase structure exists in PDB. The four available structures (2WVI, 3SI5, 4GGD, 5JJA) correspond to the N-terminal TPR domain or short fragments outside the pseudokinase region. Therefore, AlphaFold predictions are the only available structural reference for this region

### 2.4 Evidence Triangulation

Conclusions required convergence across ≥2 independent sources. Single-source findings were flagged as "forward-looking" or "exploratory" with explicit uncertainty declarations.

---

## 3. Results

### 3.1 Primary Candidate: Pimitespib/TAS-116 (HSP90 Inhibitor)

**Regulatory status**: Approved in Japan (June 2022, brand name Jeselhy) for refractory gastrointestinal stromal tumor (GIST) after failure of ≥3 prior therapies [[5]].

**Mechanistic rationale**:
- Aneuploid cells exhibit impaired HSF1/HSP90 buffering capacity, creating dependence on chaperone-mediated proteostasis [[6]]
- HSP90 inhibition destabilizes multiple oncogenic client proteins (AKT, IGF1R, mutant kinases) simultaneously, collapsing survival pathways in CIN-high cells [[7]]
- Pimitespib is **cytosolic-selective** (targets HSP90α/β), reducing ocular toxicity compared to pan-HSP90 inhibitors [[8]]

**Evidence strength** (Consensus + LeapSpace + OpenEvidence):
- Preclinical: Selective killing of aneuploid vs. euploid cells demonstrated across independent model systems [[6]]
- Clinical: Phase III CHAPTER-GIST-301 trial led to regulatory approval [[5]]
- Mechanistic: "Best mechanistic match to aneuploidy-induced proteotoxic stress" (LeapSpace) [[7]]

**Pediatric considerations**:
- No pediatric trials reported for pimitespib specifically
- Older HSP90 inhibitors (17-AAG/tanespimycin) showed limited objective activity in pediatric solid tumors with dose-limiting hepatotoxicity [[9]]
- Pimitespib's improved safety profile (less ocular toxicity, better PK) may improve pediatric tolerability, but this remains untested

**Limitations**:
- Approval limited to Japan (not FDA/EMA approved)
- Zero direct evidence in BUB1B-deficient or MVA models
- Hepatotoxicity risk requires monitoring, especially if combined with hepatotoxic chemotherapy (e.g., dactinomycin used in rhabdomyosarcoma protocols)

### 3.2 Secondary Candidate: Dasatinib (Senolytic Component)

**Regulatory status**: FDA-approved (2006) for chronic myeloid leukemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukemia (Ph+ ALL) [[10]].

**Mechanistic rationale**:
- Senolytic combination therapy (dasatinib + quercetin) clears senescent cells that accumulate after aneuploidy-induced stress [[11]]
- Senescent cells secrete pro-tumorigenic SASP (senescence-associated secretory phenotype) factors that promote bystander effects and recurrence [[12]]
- Dasatinib inhibits BCL-2 family anti-apoptotic proteins, selectively inducing apoptosis in senescent cells [[13]]

**Evidence strength** (LeapSpace + OpenEvidence):
- Preclinical: Proof-of-concept in aging and age-related disease models [[11]]
- Clinical: Early-phase trials in non-oncologic senescence-associated conditions; navitoclax (related BCL-2 inhibitor) has oncology development [[14]]
- Mechanistic: "Conceptually relevant only if SAC deficiency produces a bona fide senescent/SASP-high state" (OpenEvidence) [[14]]

**Pediatric considerations**:
- Dasatinib has established pediatric dosing for CML/ALL
- Safety profile includes hematologic dysfunction, fluid retention, QT prolongation [[15]]
- No studies in constitutional CIN syndromes

**Limitations**:
- Evidence for senolytic efficacy in aneuploidy/CIN is entirely theoretical
- Requires biomarker confirmation of senescence (cGAS-STING activation, SASP markers) before rational use
- Thrombocytopenia risk may compound chemotherapy-induced cytopenias

### 3.3 Forward-Looking Candidate: Adavosertib (WEE1 Inhibitor)

**Regulatory status**: **NOT APPROVED** by FDA or EMA. AstraZeneca discontinued clinical development program [[16]].

**Mechanistic rationale**:
- WEE1 inhibition forces premature mitotic entry with unrepaired DNA damage, causing mitotic catastrophe in replication-stressed cells [[17]]
- Exploits replication stress and checkpoint dependence in CIN-high tumors [[18]]
- Indirect mechanism: targets DNA damage response rather than proteotoxic stress directly

**Evidence strength** (LeapSpace + OpenEvidence):
- Preclinical: Synthetic lethality demonstrated in aneuploid vs. diploid breast cancer models [[18]]
- Clinical: Phase 1/2 trials in adult solid tumors (ovarian, cervical, pancreatic) [[17]]; pediatric phase 2 trial (ADVL1312) in neuroblastoma, medulloblastoma, and rhabdomyosarcoma [[19]]
- Mechanistic: "Best translational fit for chromosomal instability/replication-stress vulnerability" (LeapSpace) [[7]]

**Pediatric evidence** (Cole et al. 2023, ADVL1312 trial):
- 20 patients with neuroblastoma: 3 objective responses, met protocol-defined efficacy endpoint [[19]]
- Medulloblastoma/embryonal tumors (part C) and rhabdomyosarcoma (part D): **did NOT meet efficacy endpoints** [[19]]
- Combination with irinotecan was well tolerated with no dose-limiting toxicities [[19]]

**Why included despite non-approval**:
- Strongest pediatric translational signal among all candidates
- Real-world clinical experience in combination regimens
- Mechanistic relevance to SAC deficiency (checkpoint addiction)

**Limitations**:
- Discontinued development program limits future availability
- No efficacy signal in rhabdomyosarcoma cohort of ADVL1312 [[19]]
- Myelosuppression and diarrhea are dose-limiting in adults [[17]]

### 3.4 Forward-Looking Candidate: Sovilnesib/VLS-1488 (KIF18A Inhibitors)

**Regulatory status**: **INVESTIGATIONAL**, Phase I trials only.

**Mechanistic rationale**:
- KIF18A is a kinesin motor protein essential for mitotic spindle stabilization in chromosomally unstable cells [[20]]
- CIN-high cells show synthetic lethal dependence on KIF18A for chromosome alignment [[20]]
- Most biologically aligned with SAC/CIN deficiency among all candidates

**Evidence strength** (OpenEvidence only):
- Preclinical: Synthetic lethality specifically in chromosomally unstable tumor models [[20]]
- Clinical: Phase I completed for sovilnesib (NCT04293094), ongoing trials NCT06084416 and NCT05902988 [[20]]
- Mechanistic: "Mechanistically the most biologically aligned with SAC/CIN deficiency" (OpenEvidence) [[14]]

**Why included despite early stage**:
- Unique mechanism directly targeting CIN vulnerability
- Active clinical development (Volastra Therapeutics)
- Fills mechanistic gap not covered by HSP90/WEE1/senolytics

**Limitations**:
- Zero pediatric data or MVA-specific safety information
- No efficacy data from Phase I yet reported
- Theoretical concern: further SAC perturbation in already SAC-deficient cells could exacerbate mitotic errors in normal tissues

### 3.5 Discarded Candidates (with Justification)

**IGF-1R inhibitors (ganitumab, cixutumumab)**:
- Prior pediatric phase II trials in rhabdomyosarcoma showed modest efficacy at best [[21]]
- No mechanistic link to aneuploidy-induced proteotoxic stress [[7]]
- Repurposing rationale is RMS histology-driven, not CIN-driven [[14]]
- **Discarded**: Weak fit for mechanism-based repurposing

**Navitoclax (senolytic)**:
- Dose-limiting thrombocytopenia from BCL-xL targeting [[22]]
- Pediatric use further limited by sparse safety data [[15]]
- **Discarded**: Unacceptable toxicity profile in pediatric CIN context

**Vincristine/Vinblastine (spindle poisons)**:
- Standard components of rhabdomyosarcoma chemotherapy (VAC/IVA protocols)
- Theoretical concern: further SAC perturbation on top of germline BUB1B deficiency could amplify chromosome missegregation in surviving normal tissue [[14]]
- **NOT discarded**: Standard-of-care should not be withheld, but flagged as requiring careful monitoring

---

## 4. Discussion

### 4.1 Critical Methodological Limitations

**Gap 1: Zero Direct Evidence in BUB1B-Deficient Models**

All three independent searches converged on the same finding:
- "No retrieved study directly tested HSP90, WEE1, IGF-1R inhibitors, or senolytics in BUB1B-loss MVA models or patient-derived cells" (LeapSpace) [[7]]
- "The biggest gap is the absence of studies directly testing these agents in BUB1B-deficient or mosaic variegated aneuploidy models" (Consensus) [[6]]
- "None has been tested specifically in a child with biallelic BUB1B loss-of-function mutations" (OpenEvidence) [[14]]

**Implication**: All repurposing candidates are extrapolated from related contexts (general aneuploidy, other CIN syndromes, adult cancers). No candidate has syndrome-specific evidence.

**Gap 2: Pediatric Safety in Constitutional CIN Unknown**

Syndrome-specific toxicity data for children with constitutional chromosomal instability are missing across all drug classes [[7]]. Clinical extrapolation should assume uncertainty, not safety.

### 4.2 Structural Characterization of p.Asn1002Lys

To characterize the structural impact of the p.Asn1002Lys variant, we performed comparative structural modeling using AlphaFold 3 for both the wild-type (WT) and mutant sequences, supplemented by AlphaFold DB (O60566, model v6, pLDDT 91.06) as an orthogonal reference.

**AlphaFold 3 Comparative Analysis**:
- **Position 1002 pLDDT**: WT = 92.71 (very high confidence) vs. Mutant = 89.84 (high confidence).
- **Local destabilization**: The N1002K substitution results in a ΔpLDDT of -2.87 at the mutated site.
- **Cascading allosteric effect**: The structural perturbation propagates towards the C-terminus. Residues 1005-1007 show significantly larger confidence drops (e.g., position 1006 drops from 86.04 to 75.97, Δ = -10.06).

**Biophysical Interpretation**:
The substitution replaces Asparagine (polar, uncharged) with Lysine (basic, positively charged, bulkier) in the C-lobe of the pseudokinase domain. The observed local destabilization and C-terminal propagation suggest a disruption of the structural scaffold or protein-protein interaction interfaces (e.g., with BUB3 or CDC20), rather than loss of catalytic activity. This is entirely consistent with BubR1's established role as a catalytically inactive pseudokinase scaffold (Breit et al., 2015; Suijkerbuijk et al., 2012).

*Limitation*: Structural modeling provides a biophysical proxy for loss-of-function, not direct functional proof. The pLDDT values represent averaged atomic confidences mapped to residues.

**Note on structural references**: No experimental human BUB1B pseudokinase structure exists in PDB. The four available structures (2WVI, 3SI5, 4GGD, 5JJA) correspond to the N-terminal TPR domain or short fragments outside the pseudokinase region. Therefore, AlphaFold predictions are the only available structural reference for this region.

**Hypothesis generated by structural modeling**: p.Asn1002Lys may disrupt the scaffolding interface for BUB3/CDC20 binding or destabilize the pseudokinase fold, consistent with loss of checkpoint function. This is hypothesis-generating, not proof of pathogenicity.

**Reproducibility**:
All AlphaFold 3 job request parameters (including seeds and template configurations) and the custom Python script used for pLDDT extraction and comparison (compare_plddt_af3.py) are available in the repository (track2/structural_analysis/).

### 4.3 Clinical Implications and Recommendations

**For the current patient (PROBAND01 with rhabdomyosarcoma)**:

1. **Standard-of-care first**: VAC/IVA chemotherapy protocols should NOT be withheld based on theoretical SAC perturbation concerns. Vincristine/vinblastine remain guideline-based therapy [[14]].

2. **Pimitespib consideration**: If standard therapy fails and compassionate-use pathways are available, pimitespib represents the most mechanism-aligned approved option. Requires:
   - Hepatic function monitoring (baseline and serial LFTs)
   - Avoidance of concurrent hepatotoxic agents (e.g., dactinomycin) outside monitored trial settings [[14]]
   - Genetic tumor board consultation given constitutional CIN background

3. **Dasatinib consideration**: Only if biomarker evidence of senescence is demonstrated (e.g., cGAS-STING activation, SASP markers in tumor tissue). Empiric use without biomarker confirmation is not evidence-based.

4. **Clinical trial enrollment**: Strongly recommended if trials of WEE1 inhibitors (adavosertib) or KIF18A inhibitors (sovilnesib/VLS-1488) are available for pediatric solid tumors. These represent the most biologically rational investigational options.

### 4.4 Comparison to Alternative Approaches

**Why not IGF-1R inhibitors?**
Despite RMS lineage relevance, IGF-1R inhibitors lack mechanistic connection to aneuploidy-induced proteotoxic stress. Their modest efficacy in unselected RMS populations [[21]] and absence of CIN-specific rationale make them inferior to mechanism-aligned candidates.

**Why tier WEE1 below HSP90 despite stronger clinical data?**
Adavosertib has better pediatric translational evidence (ADVL1312 trial) [[19]], but:
1. Development program discontinued (limits future access)
2. Mechanism is indirect (replication stress, not proteotoxic stress)
3. Did not meet efficacy endpoint in rhabdomyosarcoma cohort [[19]]

Pimitespib, while having weaker pediatric data, is:
1. Approved and available (Japan)
2. Directly targets the proteotoxic stress mechanism
3. Improved safety profile over older HSP90 inhibitors

### 4.5 Red Flags and Contraindications

**Hepatotoxicity (HSP90 inhibitors)**:
- Documented liver enzyme elevation with pan-HSP90 inhibitors [[9]]
- Caution combining with hepatotoxic chemotherapy components (dactinomycin) [[14]]
- Monitoring: baseline LFTs, serial monitoring during treatment

**Myelosuppression (WEE1 inhibitors)**:
- Dose-limiting in adult trials [[17]]
- Special caution in developmentally vulnerable children [[7]]
- Monitoring: CBC with differential at baseline and weekly during treatment

**QT Prolongation (HSP90, dasatinib)**:
- Reported with some HSP90 inhibitors [[8]]
- Dasatinib carries cardiac/QT risk [[15]]
- Monitoring: baseline ECG, avoid concurrent QT-prolonging agents

---

## 5. Conclusions

This analysis proposes a tiered drug repurposing strategy for MVA1-associated rhabdomyosarcoma, prioritized by regulatory approval status and mechanistic alignment:

| Tier | Candidate | Regulatory Status | Mechanistic Alignment | Key Limitation |
|------|-----------|-------------------|----------------------|----------------|
| **Primary** | Pimitespib (HSP90) | Approved (Japan 2022) | Strong (proteotoxic stress) | No pediatric data, hepatotoxicity |
| **Secondary** | Dasatinib (senolytic) | Approved (FDA 2006) | Moderate (requires biomarker) | Theoretical evidence only |
| **Forward-looking** | Adavosertib (WEE1) | Not approved (discontinued) | Strong (replication stress) | No RMS efficacy, discontinued |
| **Forward-looking** | Sovilnesib (KIF18A) | Investigational (Phase I) | Strong (CIN-specific) | Zero pediatric data |

**Critical evidence gaps**:
- Zero direct testing in BUB1B-deficient models or MVA patients
- No pediatric safety data in constitutional CIN syndromes
- All candidates extrapolated from related contexts

**Recommendation**: Use within clinical trials or compassionate-use frameworks with multidisciplinary oversight (pediatric oncology + clinical genetics + pharmacology). Standard-of-care chemotherapy should not be withheld based on theoretical concerns.

---

## 6. AI and LLM Usage

**Alibaba Cloud Qwen 3 Max**:
- Commercial tier, standard data-handling policy
- Used as methodological reasoning assistant for search strategy design, evidence triangulation, structural analysis (AlphaFold DB pLDDT extraction), and report structuring
- Did not generate variant calls or clinical interpretations

**Anthropic Claude Sonnet**:
- Commercial terms, no training on customer content
- Used for critical review of evidence strength, identification of methodological gaps, verification of regulatory status, PDB structure verification, and clinical trial citation checking
- Provided independent verification of AlphaFold confidence scores, OMIM numbers, and literature citations

All variant calls, ACMG classifications, and clinical interpretations were made by human analysts using primary evidence (VCF, ClinVar, literature).

---

## 7. References

1. Hanks S, et al. Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. *Nat Genet*. 2004;36(11):1159-1161.
2. OMIM:257300. Mosaic Variegated Aneuploidy Syndrome 1. https://omim.org/entry/257300. OMIM:602860. BUB1B gene. https://omim.org/entry/602860
3. Suijkerbuijk SJE, van Dam TJ, Karagöz GE, von Castelmur E, Hübner NC, Duarte AMS, et al. The Vertebrate Mitotic Checkpoint Protein BUBR1 Is an Unusual Pseudokinase. *Developmental Cell*. 2012;22(6):1321-1329. doi:10.1016/j.devcel.2012.03.009. PMID: 22698286.
4. Breit C, Bange T, Petrovic A, Weir JR, Müller F, Vogt D, Musacchio A. Role of Intrinsic and Extrinsic Factors in the Regulation of the Mitotic Checkpoint Kinase Bub1. *PLoS ONE*. 2015;10(12):e0144673. doi:10.1371/journal.pone.0144673. PMID: 26658523.
5. PMDA Japan. Jeselhy (pimitespib) approval for refractory GIST. June 2022.
6. Consensus Deep Search Report. Track2_Consensus.md. 2026-09-08.
7. LeapSpace Deep Research Report. Track2_LeapSpace.md. 2026-09-08.
8. Sanchez J, et al. Old and New Approaches to Target the Hsp90 Chaperone. *Curr Cancer Drug Targets*. 2019;20(4):253-270.
9. Bagatell R, et al. Phase I pharmacokinetic and pharmacodynamic study of 17-N-allylamino-17-demethoxygeldanamycin in pediatric patients. *Clin Cancer Res*. 2007;13(19):5862-5868.
10. FDA Orange Book. Dasatinib (Sprycel) approval. 2006.
11. Kirkland JL, Tchkonia T. Senolytic drugs: from discovery to translation. *J Intern Med*. 2020;288(5):518-536.
12. Chibaya L, et al. Senescence and the tumor-immune landscape: Implications for cancer immunotherapy. *Semin Cancer Biol*. 2022;86:144-157.
13. Rad AN, Grillari J. Current senolytics: mode of action, efficacy and limitations, and their future. *Mech Ageing Dev*. 2023;213:111888.
14. OpenEvidence Clinical Synthesis. Track2_OpenEvidence.md. 2026-09-08.
15. Pediatric pharmacology reviews. Developing organs increase ADR vulnerability.
16. AstraZeneca pipeline update. Adavosertib development discontinued. 2026.
17. Leijen S, et al. Phase I study evaluating WEE1 inhibitor AZD1775 as monotherapy and in combination. *J Clin Oncol*. 2016;34(36):4371-4380.
18. Cohen-Sharir Y, Ben-David U. Relevance of aneuploidy for cancer therapies targeting the spindle assembly checkpoint and KIF18A. *Mol Cell Oncol*. 2021;8(4):1915075.
19. Cole KA, Ijaz H, Surrey LF, Santi M, Liu X, Minard CG, et al. Pediatric phase 2 trial of a WEE1 inhibitor, adavosertib (AZD1775), and irinotecan for relapsed neuroblastoma, medulloblastoma, and rhabdomyosarcoma. *Cancer*. 2023;129(14):2245-2255. PMID: 37081608.
20. Volastra Therapeutics pipeline. Sovilnesib and VLS-1488 (KIF18A inhibitors). ClinicalTrials.gov: NCT04293094, NCT06084416, NCT05902988.
21. Pappo AS, et al. A phase 2 trial of R1507, a monoclonal antibody to the insulin-like growth factor-1 receptor (IGF-1R), in patients with recurrent or refractory rhabdomyosarcoma. *Cancer*. 2014;120(7):1023-1030.
22. L'hôte V, et al. From the divergence of senescent cell fates to mechanisms and selectivity of senolytic drugs. *Open Biol*. 2022;12(11):220171.

---

## 8. Code and Data Availability

All analysis scripts, search outputs, and structural models are available at:
- GitHub: https://github.com/JoseVelasco2026/mva-hackathon-2026
- Evidence folder: /evidence/ (raw search outputs from Consensus, LeapSpace, OpenEvidence)
- Structural analysis: track2/structural_analysis/ (AlphaFold 3 outputs, pLDDT extraction scripts, job request JSONs)

---

**Conflict of Interest**: The authors declare no conflicts of interest. This analysis was performed for the MVA Hackathon 2026 educational challenge and does not constitute clinical advice.
