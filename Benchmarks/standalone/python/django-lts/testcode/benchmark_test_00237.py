# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.contrib.auth.models import User


def BenchmarkTest00237(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    parts = str(file_value).split(',')
    data = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    matches = len(User.objects.raw("SELECT * FROM users WHERE name = '" + str(processed) + "'"))
    return JsonResponse({'matches': matches}, status=200)
