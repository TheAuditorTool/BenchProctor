# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach


def to_text(value):
    return str(value).strip()

def BenchmarkTest08126(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = to_text(ua_value)
    processed = bleach.clean(markdown.markdown(data))
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
