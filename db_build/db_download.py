import subprocess

def create_db_from_fasta(fasta_file):
    cmd_list = ["mmseqs", "--help"]
    try:
        subprocess.run('bash -c "source activate cavDb; mmseqs -h"', shell=True)
    except subprocess.CalledProcessError as error:
        print("Se fue todo al carajo!")
