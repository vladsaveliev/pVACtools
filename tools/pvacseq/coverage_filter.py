import argparse
import sys
import re
import os
import csv
from lib.filter import *

def define_parser():
    parser = argparse.ArgumentParser('pvacseq coverage_filter', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'input_file',
        help="The final report .tsv file to filter"
    )
    parser.add_argument(
        'output_file',
        help="Output .tsv file containing list of filtered epitopes based on coverage and expression values"
    )
    parser.add_argument(
        '--normal-cov', type=int,
        help="Normal Coverage Cutoff. Sites above this cutoff will be considered.",
        default=5
    )
    parser.add_argument(
        '--tdna-cov', type=int,
        help="Tumor DNA Coverage Cutoff. Sites above this cutoff will be considered.",
        default=10
    )
    parser.add_argument(
        '--trna-cov', type=int,
        help="Tumor RNA Coverage Cutoff. Sites above this cutoff will be considered.",
        default=10
    )
    parser.add_argument(
        '--normal-vaf', type=float,
        help="Normal VAF Cutoff. Sites BELOW this cutoff in normal will be considered.",
        default=0.02
    )
    parser.add_argument(
        '--tdna-vaf', type=float,
        help="Tumor DNA VAF Cutoff. Sites above this cutoff will be considered.",
        default=0.25
    )
    parser.add_argument(
        '--trna-vaf', type=float,
        help="Tumor RNA VAF Cutoff. Sites above this cutoff will be considered.",
        default=0.25
    )
    parser.add_argument(
        '--expn-val', type=float,
        help="Gene and Transcript Expression cutoff. Sites above this cutoff will be considered.",
        default=1.0
    )
    parser.add_argument(
        '--exclude-NAs',
        help="Exclude NA values from the filtered output.",
        default=False,
        action='store_true'
    )
    return parser

def main(args_input = sys.argv[1:]):
    parser = define_parser()
    args = parser.parse_args(args_input)

#### COVERAGE COLUMNS ##
#Normal Depth
#Normal VAF
#Tumor DNA Depth
#Tumor DNA VAF
#Tumor RNA Depth
#Tumor RNA VAF
#Gene Expression
#Transcript Expression
    filter_criteria = []
    Filter(args.input_file, args.output_file, filter_criteria, args.exclude_NAs).execute()

if __name__ == "__main__":
    main()
