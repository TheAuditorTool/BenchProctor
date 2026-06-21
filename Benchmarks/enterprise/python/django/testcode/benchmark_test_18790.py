# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest18790(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
