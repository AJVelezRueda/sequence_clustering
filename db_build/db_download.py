import subprocess

def create_db_from_fasta(fasta_file):
    cmd = f'bash -c "source activate cavDb; mmseqs createdb {fasta_file} queryDB"'
    try:
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as error:
        print("Se rompió!")
