import subprocess, wget


def download_PDBdb(outpath):
    cmd = f"mmseqs databases PDB {outpath}/PDB {outpath}"
    try:
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as error:
        print("Something went wrong")


def download_fastaPDB(file_name):
    try:
        url = 'https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt' 
        print("Collecting data...take a Coffee or a Mate it may last long!")
        file = wget.download(url, file_name)
        print(" Finished!")
    except:
        print(" Failed to collect data!")