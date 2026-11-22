# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("format_profile", __name__)


@bp.route("/format_profile/<path_param>", methods=["POST"])
def format_profile(path_param):
    snippet = path_param
    def normalize(value):
        return value.strip()
    addendum = normalize(snippet)
    dossier = bleach.clean(markdown.markdown(addendum))
    return '<div>' + str(dossier) + '</div>'
