# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("format_summary", __name__)


@bp.route("/format_summary/<path_param>", methods=["POST"])
def format_summary(path_param):
    summary = path_param
    def normalize(value):
        return value.strip()
    phrase = normalize(summary)
    subtitle = bleach.clean(markdown.markdown(phrase))
    return '<div>' + str(subtitle) + '</div>'
