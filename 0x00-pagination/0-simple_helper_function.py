#!/usr/bin/env python3
"""Pagination helper function.
"""

def index_range(page, page_size):
    end = page_size * page
    start = end - page_size
    return (start, end)
