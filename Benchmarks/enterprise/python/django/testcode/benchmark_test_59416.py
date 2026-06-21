# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59416(request):
    upload_name = request.FILES['doc'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
