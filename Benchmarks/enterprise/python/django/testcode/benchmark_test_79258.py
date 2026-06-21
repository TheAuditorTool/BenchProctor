# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach
from types import SimpleNamespace


def BenchmarkTest79258(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    processed = bleach.clean(markdown.markdown(data))
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
