"""
Count word in given directory
"""
from collections import Counter
import linecache
import os
import psutil
import tracemalloc


def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


def iter_documents(top_directory):
    """
    Generator: iterate over all relevant documents, yielding one
    document (=list of utf8 tokens) at a time.
    https://rare-technologies.com/data-streaming-in-python-generators-iterators-iterables/
    """
    # find all .txt documents, no matter how deep under top_directory
    documents = []
    for root, dirs, files in os.walk(top_directory):
        for fname in filter(lambda fname: fname.endswith('.txt'), files):
            # read each document as one big string
            document = open(
                os.path.join(root, fname), encoding="ISO-8859-1").read()
            # Cleaning text and lower casing all words
            for char in '-.,\n':
                document = document.replace(char, ' ')

            document = document.lower()
            document_words = document.split()
            #yield fname, document_words
            documents.append((fname, document_words))
    return documents


if __name__ == "__main__":
    tracemalloc.start()
    docs_word_count = {}
    documents = iter_documents('data')
    for fname, doc in documents:
        print(fname, Counter(doc).most_common(5))
    snapshot = tracemalloc.take_snapshot()
    display_top(snapshot)
