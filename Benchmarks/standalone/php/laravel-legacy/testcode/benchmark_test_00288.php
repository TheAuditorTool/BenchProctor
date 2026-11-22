<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00288Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $sealed = base64_decode((string)$userInput, true) ?: '';
        $claims = openssl_decrypt(substr($sealed, 28), 'aes-256-gcm', getenv('DATA_ENC_KEY'), OPENSSL_RAW_DATA, substr($sealed, 0, 12), substr($sealed, 12, 16));
        return response()->json(['ok' => 1]);
    }
}
