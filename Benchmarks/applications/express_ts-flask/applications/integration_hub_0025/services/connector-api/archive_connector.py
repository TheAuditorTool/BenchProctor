# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
from urllib.parse import unquote


bp = Blueprint("archive_connector", __name__)


@bp.route("/archive_connector/<path_param>", methods=["POST"])
def archive_connector(path_param):
    footnote = path_param
    handshake = unquote(footnote)
    return '<div>' + str(handshake) + '</div>'
