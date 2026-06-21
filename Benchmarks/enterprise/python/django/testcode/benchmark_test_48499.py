# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest48499(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    os.remove(str(data))
    return JsonResponse({"saved": True})
