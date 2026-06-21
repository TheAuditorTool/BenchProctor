# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest70920(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(ua_value))
    return redirect(target)
