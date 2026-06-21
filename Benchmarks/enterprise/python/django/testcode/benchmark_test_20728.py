# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest20728(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    os.remove(str(data))
    return JsonResponse({"saved": True})
