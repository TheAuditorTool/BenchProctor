# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("build_index", __name__)


@bp.route("/build_index/<path_param>", methods=["POST"])
def build_index(path_param):
    snippet = path_param
    def normalize(value):
        return value.strip()
    montage = normalize(snippet)
    rendition = bleach.clean(markdown.markdown(montage))
    return '<div>' + str(rendition) + '</div>'
