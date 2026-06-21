# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest65713(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
