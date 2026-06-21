# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest05883(request):
    upload_name = request.FILES['upload'].name
    with open('/var/uploads/' + str(upload_name), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
