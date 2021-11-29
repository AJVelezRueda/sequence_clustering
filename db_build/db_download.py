import subprocess

def download_PDBdb(outpath):
    cmd = f"mmseqs databases PDB {outpath}/PDB {outpath}"
    try:
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as error:
        print("Se rompió!")