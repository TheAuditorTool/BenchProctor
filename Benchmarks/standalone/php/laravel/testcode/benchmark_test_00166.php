<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00166Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $ciphertext = openssl_encrypt((string)$userInput, 'des-ecb', getenv('DATA_ENC_KEY'));
        return response()->json(['ok' => 1]);
    }
}
