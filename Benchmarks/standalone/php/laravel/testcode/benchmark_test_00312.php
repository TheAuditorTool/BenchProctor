<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00312Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = sprintf('%s', $userInput);
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $requested = (int) $boundedVal;
        $allocated = $requested + 1;
        return response()->json(['allocated' => $allocated], 200);
    }
}
