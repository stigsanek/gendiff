def read_file(file_path: str) -> str:
    """
    Get file data

    :param file_path: file path
    :return: str
    """
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        return f.read()
