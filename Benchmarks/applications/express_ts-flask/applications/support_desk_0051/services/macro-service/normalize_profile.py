# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("normalize_profile", __name__)


@bp.route("/normalize_profile", methods=["POST"])
def normalize_profile():
    preface = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    grievance = normalize(preface)
    with open('/var/app/data/' + str(grievance), 'r') as fh:
        content = fh.read()
    return content
