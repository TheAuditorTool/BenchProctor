# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from types import SimpleNamespace


def BenchmarkTest30922(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
