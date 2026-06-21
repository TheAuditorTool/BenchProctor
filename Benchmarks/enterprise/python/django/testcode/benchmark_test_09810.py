# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest09810(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
