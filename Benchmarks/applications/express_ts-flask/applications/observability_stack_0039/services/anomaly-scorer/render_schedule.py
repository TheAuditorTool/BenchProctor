# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, request


bp = Blueprint("render_schedule", __name__)


@bp.route("/render_schedule", methods=["POST"])
def render_schedule():
    caption = request.headers.get('Authorization', '')
    cohort = base64.b64decode(caption).decode('utf-8', 'ignore')
    return '<div>' + str(cohort) + '</div>'
