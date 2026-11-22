# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("render_ticket", __name__)


@bp.route("/render_ticket", methods=["POST"])
def render_ticket():
    remark = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    inquiry = normalize(remark)
    grievance = os.path.join('/var/app/data', os.path.basename(inquiry))
    with open(grievance, 'r') as fh:
        content = fh.read()
    return content
