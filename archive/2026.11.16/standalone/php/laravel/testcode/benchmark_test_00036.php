<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00036Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Forwarded-For', '');
        $data = "{$userInput}";
        $iv = random_bytes(12);
        $tag = '';
        $_ct = openssl_encrypt((string)$data, 'aes-256-gcm', getenv('DATA_ENC_KEY'), 0, $iv, $tag);
        $ciphertext = base64_encode($iv . $tag . $_ct);
        return response()->json(['ok' => 1]);
    }
}
