
# LinkShot

LinkShot is a Python library designed to facilitate the management of linked files within a directory structure. It allows for easy review of files by copying them into a linked directory, and provides functionality to remove original files that are no longer linked.

*Note: this library is just a utility designed to be used in other projects.*

## Features

- **Create Linked Files**: Copies files from a source folder structure to a linked folder structure, allowing for easy review or access.
- **Flexible Extension Filtering**: Specify file extensions to include when creating links or deleting original files.
- **Hard Link or Symbolic Link**: Choose between creating hard links or symbolic links for the linked files.

## Installation

```
pip install linkshot
```

## Usage

```python
import linkshot

# Create linked files
linkshot.create(input_folder='source_folder', output_folder='linked_folder', extensions=['.txt', '.pdf'])

# Delete original files not linked anymore
linkshot.delete(source_folder='source_folder', links_folder='linked_folder', extensions=['.txt', '.pdf'])
```

## License

LinkShot is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for more details.

