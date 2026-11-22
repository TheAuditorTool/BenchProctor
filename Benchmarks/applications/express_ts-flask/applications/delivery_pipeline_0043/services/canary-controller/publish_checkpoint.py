# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("publish_checkpoint", __name__)


@bp.route("/publish_checkpoint/<path_param>", methods=["POST"])
def publish_checkpoint(path_param):
    remark = path_param
    def normalize(value):
        return value.strip()
    note = normalize(remark)
    phrase = bleach.clean(markdown.markdown(note))
    return '<div>' + str(phrase) + '</div>'
