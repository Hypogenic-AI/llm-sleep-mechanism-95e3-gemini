# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT committed to git due to size. Follow the download instructions below.

## Dataset 1: MT-Consistency
- **Source**: [yubol/MT-Consistency](https://huggingface.co/datasets/yubol/MT-Consistency)
- **Size**: 700 samples
- **Format**: HuggingFace Dataset
- **Task**: Multi-turn consistency evaluation

## Dataset 2: Long-MT-Bench-Plus
- **Source**: [panzs19/Long-MT-Bench-Plus](https://huggingface.co/datasets/panzs19/Long-MT-Bench-Plus)
- **Size**: 11 complex multi-session dialogues
- **Format**: HuggingFace Dataset
- **Task**: Long-term memory and dialogue evaluation

## Download Instructions

**Using HuggingFace:**
```python
from datasets import load_dataset
# For MT-Consistency
ds1 = load_dataset("yubol/MT-Consistency")
ds1.save_to_disk("datasets/mt_consistency")

# For Long-MT-Bench-Plus
ds2 = load_dataset("panzs19/Long-MT-Bench-Plus")
ds2.save_to_disk("datasets/long_mt_bench_plus")
```

## Loading the Dataset
```python
from datasets import load_from_disk
ds1 = load_from_disk("datasets/mt_consistency")
ds2 = load_from_disk("datasets/long_mt_bench_plus")
```
