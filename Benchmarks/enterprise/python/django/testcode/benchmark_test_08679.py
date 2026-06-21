# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach


def BenchmarkTest08679(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    processed = bleach.clean(markdown.markdown(data))
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
