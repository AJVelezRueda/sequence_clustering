import subprocess
import os, glob

def create_db_from_fasta(fasta_file):
    cmd = f'mmseqs createdb {fasta_file} queryDB'
    try:
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as error:
        print("Se rompió!")


def merge_fastas(fasta_list, final_fasta):
    for i in range(0, len(fasta_list)):
        with open(final_fasta,"a") as a_fasta:
            another_fasta = open(fasta_list[i], 'r').read()
            a_fasta.write(another_fasta)