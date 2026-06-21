# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest25098(request):
    multipart_value = request.POST.get('multipart_field', '')
    processed = html.escape(multipart_value)
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
