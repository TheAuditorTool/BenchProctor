# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest30995(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    os.seteuid(65534)
    return JsonResponse({"saved": True})
