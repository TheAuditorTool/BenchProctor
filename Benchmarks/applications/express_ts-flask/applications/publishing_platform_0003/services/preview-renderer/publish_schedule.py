# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("publish_schedule", __name__)


@bp.route("/publish_schedule", methods=["POST"])
def publish_schedule():
    heading = request.headers.get('X-Forwarded-For', '')
    addendum = heading if heading else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", addendum):
        return jsonify({'error': 'forbidden'}), 400
    byline = addendum
    Path('/var/app/data/' + str(byline)).write_text('data')
    return jsonify({"result": "success"})
