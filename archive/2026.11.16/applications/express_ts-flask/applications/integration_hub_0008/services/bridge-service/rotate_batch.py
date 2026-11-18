# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
from app_runtime import db


bp = Blueprint("rotate_batch", __name__)


@bp.route("/rotate_batch", methods=["POST"])
def rotate_batch():
    preface = db.fetch_one('SELECT name FROM users LIMIT 1')
    handshake = (lambda v: v.strip())(preface)
    return '<div>' + str(handshake) + '</div>'
