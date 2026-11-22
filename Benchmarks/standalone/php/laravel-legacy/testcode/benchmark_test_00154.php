<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00154Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = ($userInput !== null) ? $userInput : '';
        $claims = openssl_decrypt((string)$data, 'aes-256-ecb', getenv('DATA_ENC_KEY'));
        return response()->json(['ok' => 1]);
    }
}
