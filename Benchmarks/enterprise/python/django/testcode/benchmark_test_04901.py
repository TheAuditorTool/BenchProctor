# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest04901(request):
    xml_value = request.body.decode('utf-8')
    os.chmod('/var/app/data/' + str(xml_value), 0o777)
    return JsonResponse({"saved": True})
