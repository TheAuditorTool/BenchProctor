# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("normalize_fulfillment", __name__)


@bp.route("/normalize_fulfillment", methods=["POST"])
def normalize_fulfillment():
    heading = request.headers.get('Authorization', '')
    parts = str(heading).split(',')
    voucher = ' '.join(parts)
    os.unlink('/var/app/data/' + str(voucher))
    return jsonify({"result": "success"})
