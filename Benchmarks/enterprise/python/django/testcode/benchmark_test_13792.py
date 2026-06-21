# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest13792(request):
    xml_value = request.body.decode('utf-8')
    logging.info('User action: ' + str(xml_value))
    return JsonResponse({"saved": True})
