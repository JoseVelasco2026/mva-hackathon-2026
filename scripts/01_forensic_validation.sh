#!/bin/bash
# Forensic validation pipeline for BUB1B compound heterozygote
# Team: Los omikos | Author: JoseVelasco22
# Date: 2026-09-08
#
# This script reproduces the four validation checks performed on the
# BUB1B compound heterozygote finding for MVA syndrome 1.
#
# Usage: bash scripts/01_forensic_validation.sh

VCF="${1:-/mnt/e/hackathon_mva_data/WGS_EX2312012_HGWCNDSX7.vcf.gz}"
RESULTS_DIR="${2:-./exomiser_results}"

echo "=========================================="
echo "1. Phase verification (PGT/PID tags)"
echo "=========================================="
zcat "$VCF" | grep -v "^#" | \
  awk '$1=="15" && ($2==40209701 || $2==40220612)' | \
  cut -f2,9,10

echo ""
echo "=========================================="
echo "2. Coverage analysis (coarse CNV screen)"
echo "=========================================="
echo "BUB1B region (chr15:40.1-40.3Mb):"
zcat "$VCF" | grep -v "^#" | \
  awk '$1=="15" && $2>=40100000 && $2<=40300000' | \
  awk -F'\t' '{split($8,info,";"); for(i in info) if(info[i] ~ /^DP=/){split(info[i],dp,"="); print dp[2]}}' | \
  sort -n | \
  awk 'BEGIN{sum=0;count=0} {sum+=$1;count++; if($1>max)max=$1; if(min==""||$1<min)min=$1} END{printf "  min=%d max=%d mean=%.1f variants=%d\n",min,max,sum/count,count}'

echo "Control region (chr15:50.0-50.2Mb):"
zcat "$VCF" | grep -v "^#" | \
  awk '$1=="15" && $2>=50000000 && $2<=50200000' | \
  awk -F'\t' '{split($8,info,";"); for(i in info) if(info[i] ~ /^DP=/){split(info[i],dp,"="); print dp[2]}}' | \
  sort -n | \
  awk 'BEGIN{sum=0;count=0} {sum+=$1;count++; if($1>max)max=$1; if(min==""||$1<min)min=$1} END{printf "  min=%d max=%d mean=%.1f variants=%d\n",min,max,sum/count,count}'

echo ""
echo "=========================================="
echo "3. ClinVar verification"
echo "=========================================="
if [ -f "$RESULTS_DIR/mva_patient_01_expanded.variants.tsv" ]; then
  awk -F'\t' '{print "Variant:", $2, "\nExomiser ACMG:", $26, "\nClinVar ID:", $30, "\nClinVar interpretation:", $31, "\nClinVar stars:", $32}' \
    "$RESULTS_DIR/mva_patient_01_expanded.variants.tsv" | \
    grep -A4 "40209701\|40220612"
else
  echo "WARNING: variants.tsv not found. Run Exomiser first."
fi

echo ""
echo "=========================================="
echo "4. MHC/HLA artifact verification"
echo "=========================================="
if [ -f "$RESULTS_DIR/mva_patient_01_nopanel.genes.tsv" ]; then
  echo "Top 5 genes from genome-wide analysis:"
  head -6 "$RESULTS_DIR/mva_patient_01_nopanel.genes.tsv" | \
    awk -F'\t' '{printf "%s\t%s\t%s\t%s\n", $1, $3, $7, $8}'
else
  echo "WARNING: nopanel.genes.tsv not found. Run Exomiser first."
fi

echo ""
echo "=========================================="
echo "Validation complete."
echo "=========================================="
