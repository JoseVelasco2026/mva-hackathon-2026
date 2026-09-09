# Bitácora de Análisis — MVA Hackathon 2026, Track 1

## Resumen ejecutivo

**Gen causal:** BUB1B (OMIM:602789)
**Enfermedad:** Mosaic Variegated Aneuploidy syndrome 1 (OMIM:257300)
**Variantes:** Heterocigoto compuesto (trans, inferido por parsimonia funcional)
- chr15:40,209,701 T>G — p.Leu737* (nonsense, ClinVar PATHOGENIC 2 estrellas, ID 533901)
- chr15:40,220,612 T>G — p.Asn1002Lys (missense, VUS, AlphaMissense 0.923)

**Score Exomiser:** 0.9819 (pheno 0.8134, variant 0.9614)

## Cronología de análisis

### Fase 1: Configuración del entorno
- Instalación de Exomiser v14.0.0 con Java 21
- Descarga de datos de referencia: 2406_hg38 (22 GB), 2406_phenotype (9.2 GB)
- Resolución de problemas de memoria (OutOfMemoryError) con -Xmx6g

### Fase 2: Análisis dirigido (panel 22 genes)
- Configuración: PASS_ONLY, genePanelFilter con 22 genes MVA/microcefalia
- Resultado: BUB1B rank 1, score 0.9819
- Tiempo: ~1 minuto

### Fase 3: Análisis con panel expandido (51 genes)
- Configuración: PASS_ONLY, genePanelFilter con 51 genes SAC/reparación de ADN
- Resultado: BUB1B rank 1, score 0.9819 (idéntico)
- Validación: ATM (rank 3, score 0.0578) descartado como competidor

### Fase 4: Análisis genoma completo (coding + splice)
- Configuración: PASS_ONLY, variantEffectFilter (sin panel)
- Resultado: BUB1B rank 1, score 0.9819 (idéntico)
- HLA-DRB1 rank 2 (score 0.9624) descartado como artefacto de polimorfismo MHC

### Fase 5: Validación forense
1. **CNV:** Cobertura BUB1B 43.2x vs control 43.3x — consistente con número de copias diploide a escala regional; CNVs pequeños requieren caller dedicado
2. **Fase:** Las dos variantes BUB1B no tienen tags de fase (GT:AD:DP:GQ:PL; genotipos 0/1); hay PGT/PID en sitios cercanos, pero la distancia de 10.9 kb impide phasing directo por short reads
3. **Parsimonia funcional:** CIS inconsistente con fenotipo recesivo — TRANS inferido
4. **Promotor/UTR:** Sin variantes PASS en región correcta (chr15:40,159,000-40,162,000)
5. **ClinVar:** p.Leu737* confirmada con 2 estrellas (múltiples declarantes, sin conflictos)

## Limitaciones documentadas

1. Fase cis/trans inferida por parsimonia funcional, no confirmada por phasing directo
2. p.Asn1002Lys clasificada como VUS (REVEL 0.472 borderline)
3. Sin BAM disponible para CNV calling riguroso (GATK-SV/Manta)
4. Sin datos parentales para validación de segregación

## Herramientas y recursos

- Exomiser v14.0.0
- Datos de referencia: 2406_hg38, 2406_phenotype
- ClinVar (2024-06 release)
- gnomAD v2/v4
- OMIM:257300, OMIM:602789
- AlphaMissense, MVP, REVEL, SPLICE_AI

## Uso de IA/LLM

- Qwen 3 Max (Alibaba Cloud): asistente de razonamiento metodológico
- Claude (Anthropic): segunda opinión y validación cruzada
- Todos los llamados de variantes producidos por Exomiser y validados manualmente
