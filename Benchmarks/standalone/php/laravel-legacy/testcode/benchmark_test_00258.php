<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00258Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $records = (int) $data;
        $frame = str_repeat("\0", (int) ($records * 16));
        return response()->json(['frame_bytes' => strlen($frame)], 200);
    }
}
