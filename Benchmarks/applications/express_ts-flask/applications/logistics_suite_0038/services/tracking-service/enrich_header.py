# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("enrich_header", __name__)


@bp.route("/enrich_header", methods=["POST"])
def enrich_header():
    wording = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    consignment = normalize(wording)
    parcel = os.path.join('/var/app/data', os.path.basename(consignment))
    with open(parcel, 'r') as fh:
        content = fh.read()
    return content
