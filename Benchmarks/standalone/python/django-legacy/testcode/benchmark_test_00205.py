# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.parse


def BenchmarkTest00205(request):
    user_id = request.GET.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = JsonResponse({'status': 'ok'})
    resp.headers['Set-Cookie'] = 'session=' + encoded_session + '; Secure; HttpOnly; SameSite=Strict; Path=/'
    return resp
