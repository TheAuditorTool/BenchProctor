# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71523(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
