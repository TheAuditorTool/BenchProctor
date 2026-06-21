# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest04206(request):
    multipart_value = request.POST.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', multipart_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = multipart_value
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
