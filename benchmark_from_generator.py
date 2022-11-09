from datasets import IterableDataset, Features, Image, Value
from datasets.download.streaming_download_manager import ArchiveIterable
from pathlib import Path
from tqdm import tqdm
import time
import sys

root = Path(__file__).resolve().parent
warmup = 100
decode = "--decode" in sys.argv[1:]

gen_kwargs = {
    "filepaths": sorted([str(p) for p in (root / "webdataset").glob("*.tar")])
}


def gen(filepaths):
    for filepath in filepaths:
        example = {}
        curr_id = None
        for name, f in ArchiveIterable.from_urlpath(filepath):
            example_id, column_name, extension = name.split(".")
            if example_id == curr_id:
                example[column_name] = f.read()
            else:
                if example:
                    yield example
                curr_id = example_id
                example = {column_name: f.read()}
        if example:
            yield example


process = lambda x: {"image": {"bytes": x["image"], "path": "foo.jpg"}}
ds = IterableDataset.from_generator(gen, gen_kwargs=gen_kwargs).map(process)
ds = ds.cast(Features({"image": Image(decode=decode), "label": Value("int32")}))

for i, example in tqdm(enumerate(ds), unit="ex", total=10_000):
    if i == 0:
        print("First example: \t", str(example)[:500], "...")
    if i == warmup:
        _start = time.time()
_end = time.time()
total = i + 1
print(f"Done in {_end - _start:.1f}sec")
print(f"Average speed on {total} examples:\t{total / (_end - _start):.1f}examples/sec")
