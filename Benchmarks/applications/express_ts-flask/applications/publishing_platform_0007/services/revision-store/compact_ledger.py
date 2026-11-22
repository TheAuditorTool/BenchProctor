# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("compact_ledger", __name__)


@bp.route("/compact_ledger", methods=["POST"])
def compact_ledger():
    remark = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    byline = normalize(remark)
    addendum = os.path.join('/var/app/data', os.path.basename(byline))
    with open(addendum, 'r') as fh:
        content = fh.read()
    return content
