# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from urllib.parse import unquote


def BenchmarkTest27865(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
