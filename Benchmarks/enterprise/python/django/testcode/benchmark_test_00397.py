# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def coalesce_blank(value):
    return value or ''

def BenchmarkTest00397(request):
    user_id = request.GET.get('id', '')
    data = coalesce_blank(user_id)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
