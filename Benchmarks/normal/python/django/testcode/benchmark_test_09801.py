# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def ensure_str(value):
    return str(value)

def BenchmarkTest09801(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ensure_str(field_value)
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
