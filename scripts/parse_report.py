import sys
from portfolio_analyzer.parser import parse_report

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "data/parsed"
    parse_report(input_file, output_dir)
