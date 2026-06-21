# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33572(request):
    multipart_value = request.POST.get('multipart_field', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(multipart_value) + ',data\n')
    return JsonResponse({"saved": True})
