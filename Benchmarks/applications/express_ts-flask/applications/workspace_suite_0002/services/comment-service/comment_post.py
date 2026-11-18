# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("post_comment", __name__)


@bp.route("/post_comment", methods=["POST"])
def post_comment():
    summary = (request.get_json(silent=True) or {}).get("workspace_payload", "")
    passage = bleach.clean(markdown.markdown(summary))
    return '<div>' + str(passage) + '</div>'
