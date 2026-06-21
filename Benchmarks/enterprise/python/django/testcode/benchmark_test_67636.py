# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest67636(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
