from datasets import load_dataset
from pathlib import Path
from io import BytesIO

root = Path(__file__).resolve().parent
(root / "arrow").mkdir(exist_ok=True)
cache_file_name = str(root / "arrow" / "dataset.arrow")

ds = load_dataset(str(root / "imagefolder"), split="train")
def to_jpg(x):
    buffer = BytesIO()
    x["image"].save(buffer, format="JPEG", quality=100)
    return {"image": {"bytes": buffer.getvalue(), "path": "foo.jpg"}}
ds = ds.map(to_jpg, cache_file_name=cache_file_name, num_proc=4)
