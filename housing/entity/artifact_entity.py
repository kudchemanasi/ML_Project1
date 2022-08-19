from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact",
["train_file_path","test_file-path","is_ingested","message"])