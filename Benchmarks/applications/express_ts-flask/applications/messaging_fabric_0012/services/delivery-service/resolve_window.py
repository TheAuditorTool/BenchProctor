# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("resolve_window", __name__)


@bp.route("/resolve_window/<path_param>", methods=["POST"])
def resolve_window(path_param):
    preface = path_param
    def normalize(value):
        return value.strip()
    bulletin = normalize(preface)
    citation = bleach.clean(markdown.markdown(bulletin))
    return '<div>' + str(citation) + '</div>'
