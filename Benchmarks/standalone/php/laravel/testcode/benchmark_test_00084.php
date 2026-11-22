<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00084Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Forwarded-For', '');
        $hashCtx = hash_init('md4');
        hash_update($hashCtx, (string)$userInput);
        $digest = hash_final($hashCtx);
        return response()->json(['ok' => 1]);
    }
}
