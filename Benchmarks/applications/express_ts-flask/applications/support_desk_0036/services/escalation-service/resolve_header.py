# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("resolve_header", __name__)


@bp.route("/resolve_header", methods=["POST"])
def resolve_header():
    preface = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    grievance = normalize(preface)
    inquiry = os.path.join('/var/app/data', os.path.basename(grievance))
    with open(inquiry, 'r') as fh:
        content = fh.read()
    return content
