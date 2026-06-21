# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import json
from app_runtime import db


def BenchmarkTest58624():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    return render_template_string('safe block: {{ value }}', value=data)
