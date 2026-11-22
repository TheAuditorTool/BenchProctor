# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("validate_checkpoint", __name__)


@bp.route("/validate_checkpoint/<path_param>", methods=["POST"])
def validate_checkpoint(path_param):
    synopsis = path_param
    def normalize(value):
        return value.strip()
    rendition = normalize(synopsis)
    montage = bleach.clean(markdown.markdown(rendition))
    return '<div>' + str(montage) + '</div>'
