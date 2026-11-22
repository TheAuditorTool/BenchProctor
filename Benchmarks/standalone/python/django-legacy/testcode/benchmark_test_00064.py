# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from pathlib import Path


def BenchmarkTest00064(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", ua_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = ua_value
    Path('/var/app/data/' + str(processed)).write_text('data')
    return JsonResponse({"saved": True})
