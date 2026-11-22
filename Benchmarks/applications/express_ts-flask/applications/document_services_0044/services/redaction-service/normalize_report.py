# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("normalize_report", __name__)


@bp.route("/normalize_report", methods=["POST"])
def normalize_report():
    phrase = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    dossier = normalize(phrase)
    addendum = os.path.join('/var/app/data', os.path.basename(dossier))
    with open(addendum, 'r') as fh:
        content = fh.read()
    return content
