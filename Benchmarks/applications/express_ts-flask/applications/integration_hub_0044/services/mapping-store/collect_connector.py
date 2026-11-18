# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("collect_connector", __name__)


@bp.route("/collect_connector/<path_param>", methods=["POST"])
def collect_connector(path_param):
    blurb = path_param
    handshake, _sep, _rest = str(blurb).partition('\x00')
    citation = bleach.clean(markdown.markdown(handshake))
    return '<div>' + str(citation) + '</div>'
