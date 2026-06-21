# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest52108(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    os.remove(str(data))
    return JsonResponse({"saved": True})
