# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest72819(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
