# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from django import forms
from types import SimpleNamespace


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest52876(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
