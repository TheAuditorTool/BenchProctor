<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00315Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $ciphertext = openssl_encrypt((string)$data, 'des-ecb', getenv('DATA_ENC_KEY'));
        return response()->json(['ok' => 1]);
    }
}
