# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("normalize_batch", __name__)


@bp.route("/normalize_batch", methods=["POST"])
def normalize_batch():
    transcript = request.headers.get('Referer', '')
    reader = make_reader(transcript)
    parcel = reader()
    consignment = bleach.clean(markdown.markdown(parcel))
    return '<div>' + str(consignment) + '</div>'
