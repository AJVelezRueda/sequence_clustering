import argparse

from db_build.db_download import create_db_from_fasta


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fasta_db_file', 
        type=str,
        help='path of the Fasta file to convert to a mmseqs parseable db')
    
    args = parser.parse_args()
    
    create_db_from_fasta(args.fasta_db_file)
    
if __name__ == "__main__":
    main()