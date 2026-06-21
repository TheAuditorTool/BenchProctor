# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest78918(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
