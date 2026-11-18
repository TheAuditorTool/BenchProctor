# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("audit_report", __name__)


@bp.route("/audit_report", methods=["POST"])
def audit_report():
    citation = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    parcel = ','.join(parts)
    if parcel not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    consignment = parcel
    subprocess.Popen('echo ' + str(consignment), shell=True).wait()
    return jsonify({"result": "success"})
