# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest73443(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
