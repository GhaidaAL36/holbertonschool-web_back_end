#!/usr/bin/env python3
"""Module for paginating a database of popular baby names."""

import csv
import math
from typing import List


def index_range(page, page_size):
    """Return a tuple of start and end indexes for the given pagination parameters.

    Args:
        page: the page number (1-indexed)
        page_size: the number of items per page

    Returns:
        A tuple (start, end) representing the range of indexes.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset, loading from CSV if necessary."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset.

        Args:
            page: the page number to retrieve (1-indexed, default 1)
            page_size: the number of items per page (default 10)

        Returns:
            A list of rows for the requested page, or an empty list if out of range.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
