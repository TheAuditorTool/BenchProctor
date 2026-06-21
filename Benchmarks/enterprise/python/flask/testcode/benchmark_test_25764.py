# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest25764():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = normalise_input(comment_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
