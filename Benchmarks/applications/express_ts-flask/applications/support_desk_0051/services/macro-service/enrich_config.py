# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("enrich_config", __name__)


@bp.route("/enrich_config", methods=["POST"])
def enrich_config():
    preface = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    grievance = normalize(preface)
    inquiry = os.path.join('/var/app/data', os.path.basename(grievance))
    with open(inquiry, 'r') as fh:
        content = fh.read()
    return content
