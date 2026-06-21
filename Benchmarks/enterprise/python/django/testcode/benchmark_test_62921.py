# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest62921(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
