from datasets import load_dataset, Features, Image, Value
from pathlib import Path

root = Path(__file__).resolve().parent

ds = load_dataset(str(root / "imagefolder"), streaming=True, drop_labels=True, split="train")
ds = ds.map(lambda _: {"label": 0})
ds = ds.cast(Features({"image": Image(), "label": Value("int32")}))
ds.to_wds(str(root / "webdataset"))
