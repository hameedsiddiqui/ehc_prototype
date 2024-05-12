import argparse
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd

import flwr as fl

from flwr_datasets import FederatedDataset
from datasets import load_dataset
from flwr_datasets.partitioner import ChosenPartitioner

from ../models/nb/nb.py import run



def compute_hist(df: pd.DataFrame, col_name: str) -> np.ndarray:
    freqs, _ = np.histogram(df[col_name])
    return freqs


# Define Flower client
class FlowerClient(fl.client.NumPyClient, folder):
    def __init__(self, X: pd.DataFrame):
        self.X = X

    def fit(
        self, parameters: List[np.ndarray], config: Dict[str, str]
    ) -> Tuple[List[np.ndarray], int, Dict]:
        hist_list = run(folder)

        return (
            hist_list,
            len(self.X),
            {},
        )


if __name__ == "__main__":
    N_CLIENTS = 2
    folder = "client_1"

    parser = argparse.ArgumentParser(description="Flower")
    parser.add_argument(
        "--partition-id",
        type=int,
        choices=range(0, N_CLIENTS),
        required=True,
        help="Specifies the partition id of artificially partitioned datasets.",
    )
    args = parser.parse_args()
    partition_id = args.partition_id

    # Load the partition data
    dataset = load_dataset(f"{folder}", data_dir="/train")
    partitioner = ChosenPartitioner()
    partitioner.dataset = dataset
    partition = partitioner.load_partition(partition_id=0)
    # Use just the specified columns

    # Start Flower client
    fl.client.start_client(
        server_address="127.0.0.1:8080",
        client=FlowerClient(partition, folder).to_client(),
    )
