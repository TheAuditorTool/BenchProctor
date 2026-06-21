# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest72304(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
