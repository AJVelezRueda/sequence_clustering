import argparse

from db_build.db_build import create_db_from_fasta, merge_fastas


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fasta_db_file', 
        type=str,
        help='path of the Fasta file to convert to a mmseqs parseable db')
    
    args = parser.parse_args()
    
    create_db_from_fasta(args.fasta_db_file)

    merge_fastas(['./data/un_fasta.fasta', './data/otro_fasta.fasta'], './data/final_fasta.fasta')
    
if __name__ == "__main__":
    main()