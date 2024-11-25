#!/usr/bin/env python3

import pymupdf as pdf
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Merge multiple PDFs into a single PDF file.")
parser.add_argument(
    "-f", "--files",
    nargs='+',  # Allows multiple filenames
    required=True,
    help="List of PDF files to merge"
)
parser.add_argument(
    "-o", "--output",
    required=True,
    help="The name of the output merged PDF file"
)

# Parse arguments
args = parser.parse_args()
print("Files to merge:", args.files)
print("Output file:", args.output)



if args.files:
    try:
        first = pdf.open(args.files[0])
        for i in range(1, len(args.files)):
            current = pdf.open(args.files[i])
            first.insert_pdf(current)
        
        first.save(args.output)

    except FileNotFoundError as e:
        print(f"File not found! : {e}")