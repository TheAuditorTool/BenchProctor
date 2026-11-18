# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def BenchmarkTest00144(request):
    multipart_value = request.POST.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    return redirect(str(data))
