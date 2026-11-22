<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00011Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $digestBytes = sodium_crypto_generichash((string)$userInput);
        $digest = sodium_bin2hex($digestBytes);
        return response()->json(['ok' => 1]);
    }
}
