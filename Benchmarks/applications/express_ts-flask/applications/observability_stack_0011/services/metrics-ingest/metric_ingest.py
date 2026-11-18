# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("ingest_metric", __name__)


@bp.route("/ingest_metric", methods=["POST"])
def ingest_metric():
    heading = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    return '<div>' + str(heading) + '</div>'
