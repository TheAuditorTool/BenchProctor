# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02621(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    os.remove(str(data))
    return JsonResponse({"saved": True})
