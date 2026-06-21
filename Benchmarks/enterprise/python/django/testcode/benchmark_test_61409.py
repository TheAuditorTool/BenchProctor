# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest61409(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
