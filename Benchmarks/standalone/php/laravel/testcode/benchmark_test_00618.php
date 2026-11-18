<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00618Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $ciphertext = openssl_encrypt((string)$data, 'des-ecb', getenv('DATA_ENC_KEY'));
        return response()->json(['ok' => 1]);
    }
}
