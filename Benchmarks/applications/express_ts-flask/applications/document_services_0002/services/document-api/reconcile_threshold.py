# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("reconcile_threshold", __name__)


@bp.route("/reconcile_threshold", methods=["POST"])
def reconcile_threshold():
    wording = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(wording)
    dossier = os.path.join('/var/app/data', os.path.basename(addendum))
    with open(dossier, 'r') as fh:
        content = fh.read()
    return content
