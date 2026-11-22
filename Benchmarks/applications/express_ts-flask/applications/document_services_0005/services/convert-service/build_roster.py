# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, render_template_string


request_state: dict[str, str] = {}

bp = Blueprint("build_roster", __name__)


@bp.route("/build_roster/<path_param>", methods=["POST"])
def build_roster(path_param):
    footnote = path_param
    request_state['last_input'] = footnote
    addendum = request_state['last_input']
    return render_template_string('<div>{{ value|safe }}</div>', value=str(addendum))
