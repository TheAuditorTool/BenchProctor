# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("reconcile_checkpoint", __name__)


@bp.route("/reconcile_checkpoint", methods=["POST"])
def reconcile_checkpoint():
    excerpt = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    verdict = normalize(excerpt)
    grievance = os.path.join('/var/app/data', os.path.basename(verdict))
    with open(grievance, 'r') as fh:
        content = fh.read()
    return content
