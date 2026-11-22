# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("verify_threshold", __name__)


@bp.route("/verify_threshold", methods=["POST"])
def verify_threshold():
    transcript = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    consignment = normalize(transcript)
    parcel = os.path.join('/var/app/data', os.path.basename(consignment))
    with open(parcel, 'r') as fh:
        content = fh.read()
    return content
