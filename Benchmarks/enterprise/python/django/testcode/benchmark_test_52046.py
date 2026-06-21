# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def to_text(value):
    return str(value).strip()

def BenchmarkTest52046(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = to_text(multipart_value)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
