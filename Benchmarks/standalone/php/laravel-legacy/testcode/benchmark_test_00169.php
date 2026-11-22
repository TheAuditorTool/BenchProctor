<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00169Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $data = vsprintf('%1$s', [$userInput]);
        $hashCtx = hash_init('sha256');
        hash_update($hashCtx, (string)$data);
        $digest = hash_final($hashCtx);
        return response()->json(['ok' => 1]);
    }
}
