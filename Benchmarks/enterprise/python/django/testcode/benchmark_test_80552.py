# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest80552(request):
    upload_name = request.FILES['doc'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
