# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re


def BenchmarkTest11238(request):
    upload_name = request.FILES['upload'].name
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = upload_name
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
