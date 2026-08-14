import re


def fixed_size_chunking(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - overlap

    return chunks


def sentence_chunking(
    text: str,
    sentences_per_chunk: int = 5
):

    sentences = re.split(
        r'(?<=[.!?])\s+',
        text
    )

    chunks = []

    for i in range(
        0,
        len(sentences),
        sentences_per_chunk
    ):

        chunk = " ".join(
            sentences[
                i:i + sentences_per_chunk
            ]
        ).strip()

        if chunk:
            chunks.append(chunk)

    return chunks