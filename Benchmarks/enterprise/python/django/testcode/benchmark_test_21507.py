# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def ensure_str(value):
    return str(value)

def BenchmarkTest21507(request):
    upload_name = request.FILES['upload'].name
    data = ensure_str(upload_name)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
