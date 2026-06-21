# SPDX-License-Identifier: Apache-2.0
import json
from app_runtime import db


def BenchmarkTest11146():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = json.loads(profile_value).get('value', profile_value)
    except (json.JSONDecodeError, AttributeError):
        data = profile_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
