# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.parse


def BenchmarkTest00009(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = JsonResponse({'status': 'ok'})
    resp.headers['Set-Cookie'] = 'session=' + encoded_session + '; HttpOnly; SameSite=Strict; Path=/'
    return resp
