import os


def create(input_folder: str, output_folder: str, extensions: list[str], hard_link: bool = True):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_folder, file)
                if not os.path.exists(output_file_path) and not os.path.islink(output_file_path):
                    if hard_link:
                        os.link(input_file_path, output_file_path)
                    else:
                        os.symlink(input_file_path, output_file_path)


def delete(source_folder: str, links_folder: str, extensions: list[str]):
    def get_all_files_with_extensions(folder):
        files_set = set()
        for _root, _, _files in os.walk(folder):
            for _file in _files:
                if any(_file.endswith(ext) for ext in extensions):
                    _files_set.add(os.path.relpath(os.path.join(_root, _file), folder))  # noqa
        return files_set

    linked_files = get_all_files_with_extensions(links_folder)

    for root, _, files in os.walk(source_folder):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                if file not in linked_files:
                    os.remove(os.path.join(root, file))
