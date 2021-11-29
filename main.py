import argparse

from db_build.db_build import create_db_from_fasta, merge_fastas
from db_build.db_download import download_PDBdb


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fasta_db_file', 
        type=str,
        required=False,
        help='path of the Fasta file to convert to a mmseqs parseable db')

    parser.add_argument('--fasta_files_list', 
        nargs='+', 
        default=[],
        required=False,
        help='path to the fasta files to merge sepatared by an space')

    parser.add_argument('--download_PDB', 
        type=str,
        required=False,
        help='path to the output path')
    
    args = parser.parse_args()

    if args.fasta_db_file:   
        create_db_from_fasta(args.fasta_db_file)
    elif args.fasta_files_list: 
        merge_fastas(args.fasta_files_list, './data/final_fasta.fasta')
    elif args.download_PDB: 
        download_PDBdb(args.download_PDB)
    else:
        parser.print_help()
 

if __name__ == "__main__":
    main()