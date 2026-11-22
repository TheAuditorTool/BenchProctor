# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("reconcile_digest", __name__)


@bp.route("/reconcile_digest/<path_param>", methods=["POST"])
def reconcile_digest(path_param):
    caption = path_param
    def normalize(value):
        return value.strip()
    synopsis = normalize(caption)
    snippet = bleach.clean(markdown.markdown(synopsis))
    return '<div>' + str(snippet) + '</div>'
