# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75798(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
