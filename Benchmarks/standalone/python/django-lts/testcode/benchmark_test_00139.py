# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def BenchmarkTest00139(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.unlink('/var/app/data/' + str(processed))
    return JsonResponse({"saved": True})
