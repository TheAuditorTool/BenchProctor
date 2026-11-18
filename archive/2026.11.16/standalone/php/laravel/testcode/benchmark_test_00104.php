<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00104Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $data = hex2bin($userInput);
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $requested = (int) $boundedVal;
        $allocated = $requested + 1;
        return response()->json(['allocated' => $allocated], 200);
    }
}
