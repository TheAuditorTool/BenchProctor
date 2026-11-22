# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("validate_comment", __name__)


@bp.route("/validate_comment", methods=["POST"])
def validate_comment():
    caption = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    synopsis = normalize(caption)
    snippet = os.path.join('/var/app/data', os.path.basename(synopsis))
    with open(snippet, 'r') as fh:
        content = fh.read()
    return content
