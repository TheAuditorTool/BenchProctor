# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest01229(request):
    field_value = UserForm(request.POST).data.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return JsonResponse({'error': 'invalid file type'}, status=400)
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
