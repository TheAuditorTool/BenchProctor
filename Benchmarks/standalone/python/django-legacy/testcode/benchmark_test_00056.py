# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse


def BenchmarkTest00056(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
