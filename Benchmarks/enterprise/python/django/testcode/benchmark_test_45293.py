# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from types import SimpleNamespace


def BenchmarkTest45293(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
