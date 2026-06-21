# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def BenchmarkTest09650(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
