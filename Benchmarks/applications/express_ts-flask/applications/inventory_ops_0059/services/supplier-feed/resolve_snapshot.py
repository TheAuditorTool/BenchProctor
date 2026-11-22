# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("resolve_snapshot", __name__)


@bp.route("/resolve_snapshot", methods=["POST"])
def resolve_snapshot():
    memo = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    backorder = normalize(memo)
    restock = os.path.join('/var/app/data', os.path.basename(backorder))
    with open(restock, 'r') as fh:
        content = fh.read()
    return content
