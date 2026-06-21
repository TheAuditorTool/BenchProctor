# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest39198(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
