# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest76546(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
