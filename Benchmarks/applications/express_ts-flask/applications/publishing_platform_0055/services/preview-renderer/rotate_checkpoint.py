# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("rotate_checkpoint", __name__)


@bp.route("/rotate_checkpoint/<path_param>", methods=["POST"])
def rotate_checkpoint(path_param):
    synopsis = path_param
    def normalize(value):
        return value.strip()
    byline = normalize(synopsis)
    addendum = bleach.clean(markdown.markdown(byline))
    return '<div>' + str(addendum) + '</div>'
