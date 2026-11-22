# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("audit_device", __name__)


@bp.route("/audit_device", methods=["POST"])
def audit_device():
    paragraph = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    persona = normalize(paragraph)
    blurb = os.path.join('/var/app/data', os.path.basename(persona))
    with open(blurb, 'r') as fh:
        content = fh.read()
    return content
