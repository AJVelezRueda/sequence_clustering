## Intallation

```bash
# Create and active a virtual conda venv
$ conda env create --file env.yml
# For activating the environment use
$ conda activate cavDb
# For deactivating the environment use
$ conda deactivate
```


## Running CavDB

```bash
#Activate the conda venv
$ conda activate cavDB
#for merging multiple fasta files
$ python main.py --fasta_files_list ./data/un_fasta.fasta ./data/otro_fasta.fasta
#for creating a db from a fasta file
$ python main.py --fasta_db_file ./data/QUERY.fasta
#for downloading PDB
$ python main.py --download_PDB PDB
```