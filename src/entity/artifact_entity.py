"""
Artifact says:

“These files WERE created successfully”
"""

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
