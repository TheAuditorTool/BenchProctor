<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00198Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $ciphertext = openssl_encrypt((string)$data, 'des-ecb', getenv('DATA_ENC_KEY'));
        return response()->json(['ok' => 1]);
    }
}
