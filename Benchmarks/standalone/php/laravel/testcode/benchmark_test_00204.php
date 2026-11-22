<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00204Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $data = vsprintf('%1$s', [$userInput]);
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $records = (int) $boundedVal;
        $frame = str_repeat("\0", (int) ($records * 16));
        return response()->json(['frame_bytes' => strlen($frame)], 200);
    }
}
