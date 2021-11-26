import argparse

from db_build.db_download import create_db_from_fasta


def main():
    create_db_from_fasta("./data/QUERY.fasta")

if __name__ == "__main__":
    main()