# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest17634(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
