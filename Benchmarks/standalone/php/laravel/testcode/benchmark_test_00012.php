<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00012Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        $data = (!empty($userInput)) ? $userInput : '';
        $digestBytes = sodium_crypto_generichash((string)$data);
        $digest = sodium_bin2hex($digestBytes);
        return response()->json(['ok' => 1]);
    }
}
