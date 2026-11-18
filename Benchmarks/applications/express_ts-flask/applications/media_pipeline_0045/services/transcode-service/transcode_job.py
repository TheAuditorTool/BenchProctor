# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("enqueue_transcode", __name__)


@bp.route("/enqueue_transcode", methods=["POST"])
def enqueue_transcode():
    note = (request.get_json(silent=True) or {}).get("media_payload", "")
    return '<div>' + str(note) + '</div>'
