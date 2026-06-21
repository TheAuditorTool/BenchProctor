# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
_shared_counter_lock = threading.Lock()

def BenchmarkTest30292(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % (field_value,)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
