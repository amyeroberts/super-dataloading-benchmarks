# Super-dataloading benchmarks

## Setup

```bash
pip install -r requirements.txt
python prepare_imagefolder.py
python prepare_webdataset.py
python prepare_arrow.py
```

Each script prepares the data in a certain format:

- `prepare_imagefolder` downloads 10k images from imagenet into one folder
- `prepare_webdataset` prepares the 10k images in 4 webdataset shards (TAR) using JPEG/quality=100 from the images from `prepare_imagefolder`
- `prepare_arrow` prepares the 10k images in 4 `datasets` arrow shards using JPEG/quality=100 from the images from `prepare_imagefolder`

## Run

```bash
python benchmark_imagefolder.py
python benchmark_webdataset.py
python benchmark_arrow.pypy
python benchmark_from_generator.py
```

Each benchmark computes the average examples/sec using a single process:

- `benchmark_imagefolder` uses `datasets` and the local images
- `benchmark_webdataset` uses the webdataset data
- `benchmark_arrow` uses `datasets` and the arrow data
- `benchmark_from_generator` uses `datasets` IterableDataset.from_generator and the TAR data

## Results

TBA
