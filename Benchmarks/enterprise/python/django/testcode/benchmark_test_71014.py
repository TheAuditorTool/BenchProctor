# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def BenchmarkTest71014(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(profile_value)
    data = collected
    processed = re.sub(r'\d+', '****', str(data))
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
