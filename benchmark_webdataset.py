from webdataset import WebDataset
from pathlib import Path
from tqdm import tqdm
import time
import sys

root = Path(__file__).resolve().parent
warmup = 100
decode = "--decode" in sys.argv[1:]

filepaths = sorted([str(p) for p in (root / "webdataset").glob("*.tar")])
ds = WebDataset(filepaths)
if decode:
    ds = ds.decode("pil").to_tuple("image.jpg", "label.id")

for i, example in tqdm(enumerate(ds), unit="ex"):
    if i == 0:
        print("First example: \t", str(example)[:500], "...")
    if i == warmup:
        _start = time.time()
_end = time.time()
total = i + 1
print(f"Done in {_end - _start:.1f}sec")
print(f"Average speed on {total} examples:\t{total / (_end - _start):.1f}examples/sec")
