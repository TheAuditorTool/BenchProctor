# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest67172(request):
    multipart_value = request.POST.get('multipart_field', '')
    with open('/var/uploads/' + str(multipart_value), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
