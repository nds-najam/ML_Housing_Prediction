from collections import namedtuple


DataIngestionArtefact = namedtuple("DataIngestionArtefact",["train_file_path","test_file_path","is_ingested", "message"])