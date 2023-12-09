import pandas as pd
import json

from datasets import load_dataset

dataset = load_dataset("HuggingFaceH4/CodeAlpaca_20K")
train_list = list(dataset["train"])
test_list = list(dataset["test"])

with open("data.jsonl", "w") as f:
    for item in train_list + test_list:
        json.dump(item, f)
        f.write("\n")