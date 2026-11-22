<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00305Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = str_replace("\0", '', $userInput);
        $sealed = base64_decode((string)$data, true) ?: '';
        $claims = openssl_decrypt(substr($sealed, 28), 'aes-256-gcm', getenv('DATA_ENC_KEY'), OPENSSL_RAW_DATA, substr($sealed, 0, 12), substr($sealed, 12, 16));
        return response()->json(['ok' => 1]);
    }
}
