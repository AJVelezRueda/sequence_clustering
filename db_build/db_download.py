import subprocess, requests


def download_PDBdb(outpath):
    cmd = f"mmseqs databases PDB {outpath}/PDB {outpath}"
    try:
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as error:
        print("Se rompió!")


def download_fastaPDB(out_path):
    try:
        url = 'https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt' 
        r = requests.get(url)
        open("pdb_seqres.txt", 'wb').write(r.content)
    except:
        print("Se rompió!")