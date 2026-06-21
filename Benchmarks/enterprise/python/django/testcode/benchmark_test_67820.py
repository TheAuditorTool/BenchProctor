# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest67820(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    os.seteuid(65534)
    return JsonResponse({"saved": True})
