# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest67755(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
