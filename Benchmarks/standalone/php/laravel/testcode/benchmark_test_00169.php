<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00169Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $hashCtx = hash_init('md4');
        hash_update($hashCtx, (string)$data);
        $digest = hash_final($hashCtx);
        return response()->json(['ok' => 1]);
    }
}
