import argparse

from db_build.db_build import create_db_from_fasta, merge_fastas
from db_build.db_download import download_PDBdb, download_fastaPDB
from clustering_seqs.clustering_seqs import clustering_huge_data_seqs


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

    parser.add_argument('--download_fastaPDB', 
        type=str,
        required=False,
        help='complete path to the PDBs fasta output name')

    parser.add_argument('--clustering_seqs', 
        nargs='+', 
        default=[],
        required=False,
        help='path to the fasta file to cluster and the output directory name sepatared by an space')
    
    args = parser.parse_args()

    if args.fasta_db_file:   
        create_db_from_fasta(args.fasta_db_file)
    elif args.fasta_files_list: 
        merge_fastas(args.fasta_files_list, './data/final_fasta.fasta')
    elif args.download_PDB: 
        download_PDBdb(args.download_PDB)
    elif args.download_fastaPDB: 
        download_fastaPDB(args.download_fastaPDB)
    elif args.clustering_seqs:
        clustering_huge_data_seqs(args.clustering_seqs[0],args.clustering_seqs[1])
    else:
        parser.print_help()
 

if __name__ == "__main__":
    main()