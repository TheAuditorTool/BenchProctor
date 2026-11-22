<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00018Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $data = json_decode($userInput, true)['value'] ?? '';
        $digestBytes = sodium_crypto_generichash((string)$data);
        $digest = sodium_bin2hex($digestBytes);
        return response()->json(['ok' => 1]);
    }
}
