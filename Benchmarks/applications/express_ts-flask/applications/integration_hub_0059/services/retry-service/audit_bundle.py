# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("audit_bundle", __name__)


@bp.route("/audit_bundle/<path_param>", methods=["POST"])
def audit_bundle(path_param):
    synopsis = path_param
    handshake, _sep, _rest = str(synopsis).partition('\x00')
    memo = bleach.clean(markdown.markdown(handshake))
    return '<div>' + str(memo) + '</div>'
