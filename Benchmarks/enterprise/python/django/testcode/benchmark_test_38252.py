# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest38252(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
