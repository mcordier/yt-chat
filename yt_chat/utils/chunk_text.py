def get_text_chunks(text: str, chunk_size: int = 2000, chunk_overlap: int = 200) -> str:
    """
    Split text into chunks for processing.

    Parameters:
        text (str): The text to be split.
        chunk_size (int): Size of each chunk.
        chunk_overlap (int): Overlap between adjacent chunks.

    Returns:
        list: List of text chunks (strings).
    """
    chunks = []
    start = 0
    print("start chunking")
    while start < len(text):
        end = min(start + chunk_size, len(text))
        print(start, end)
        chunks.append(text[start:end])
        start = max(end, end - chunk_overlap)
    print("finish chunking")
    return chunks