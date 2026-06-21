# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from urllib.parse import unquote


def BenchmarkTest61613(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
