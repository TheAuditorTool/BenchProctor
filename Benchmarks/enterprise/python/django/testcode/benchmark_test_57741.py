# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from urllib.parse import unquote


def BenchmarkTest57741(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
