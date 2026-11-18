<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00596Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $ciphertext = openssl_encrypt((string)$data, 'des-ecb', getenv('DATA_ENC_KEY'));
        return response()->json(['ok' => 1]);
    }
}
