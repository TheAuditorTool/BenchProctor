# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest11471(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
