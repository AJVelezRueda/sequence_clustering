import subprocess

def clustering_huge_data_seqs(file, output_dir):
    cmd = f"mmseqs easy-linclust {file} {file}_clust {output_dir}"

    try:
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as error:
        print("Se rompió!")