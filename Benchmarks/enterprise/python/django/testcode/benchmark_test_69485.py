# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest69485(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
