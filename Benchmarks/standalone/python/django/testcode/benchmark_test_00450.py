# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00450(request):
    field_value = request.POST.get('field', '')
    data = field_value if field_value else 'default'
    return redirect(str(data))
