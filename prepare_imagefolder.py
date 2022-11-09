from datasets import load_dataset
from pathlib import Path
from tqdm import tqdm

print("downloading 10k images")
revision = "924f819d1060140090b89f187a935f61b0e2954c"  # for reproducibility
imgnt = load_dataset("imagenet-1k", streaming=True, split="train", revision=revision).shuffle(seed=42)
subset = list(imgnt.take(10_000))

print("saving 10k images to ./imagefolder")
d = Path(__file__).resolve() / "imagefolder"
d.mkdir(exist_ok=True)
for i, x in enumerate(tqdm(subset, total=10_000)):
    x["image"].save(d / f"{i:05d}.png")
