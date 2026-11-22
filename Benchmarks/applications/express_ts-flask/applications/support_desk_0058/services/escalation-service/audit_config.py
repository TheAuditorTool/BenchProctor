# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("audit_config", __name__)


@bp.route("/audit_config", methods=["POST"])
def audit_config():
    snippet = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    inquiry = normalize(snippet)
    grievance = os.path.join('/var/app/data', os.path.basename(inquiry))
    with open(grievance, 'r') as fh:
        content = fh.read()
    return content
