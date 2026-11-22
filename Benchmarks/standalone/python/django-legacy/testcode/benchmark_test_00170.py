# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse


def BenchmarkTest00170(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name!s}'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
