# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from urllib.parse import unquote


def BenchmarkTest00213(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
