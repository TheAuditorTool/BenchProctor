# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import re


def BenchmarkTest38793(request):
    upload_name = request.FILES['upload'].name
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(upload_name)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = upload_name
    return HttpResponse(Template(processed).render(Context()))
