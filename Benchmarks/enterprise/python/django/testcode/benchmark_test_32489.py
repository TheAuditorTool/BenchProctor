# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest32489(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
