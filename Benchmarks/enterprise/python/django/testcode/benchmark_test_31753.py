# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest31753(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = coalesce_blank(host_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
