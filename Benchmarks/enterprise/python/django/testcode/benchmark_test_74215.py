# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest74215(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
