# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse
from types import SimpleNamespace


def BenchmarkTest65354(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
