# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest64095():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = '%s' % (profile_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
