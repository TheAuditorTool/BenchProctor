# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest71468(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    os.remove(str(data))
    return JsonResponse({"saved": True})
