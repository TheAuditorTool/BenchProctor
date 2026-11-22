<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00309Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $hashCtx = hash_init('sha256');
        hash_update($hashCtx, (string)$data);
        $digest = hash_final($hashCtx);
        return response()->json(['ok' => 1]);
    }
}
