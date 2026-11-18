# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("run_conversion", __name__)


@bp.route("/run_conversion", methods=["POST"])
def run_conversion():
    headline = (request.get_json(silent=True) or {}).get("documents_payload", "")
    addendum = bleach.clean(markdown.markdown(headline))
    return '<div>' + str(addendum) + '</div>'
