# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest16146(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
