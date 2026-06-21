# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest60873(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
