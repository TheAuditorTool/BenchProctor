<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00527Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $data = vsprintf('%1$s', [$userInput]);
        $ciphertext = openssl_encrypt((string)$data, 'des-ecb', getenv('DATA_ENC_KEY'));
        return response()->json(['ok' => 1]);
    }
}
