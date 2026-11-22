<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00188Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $records = (int) $boundedVal;
        $frame = str_repeat("\0", (int) ($records * 16));
        return response()->json(['frame_bytes' => strlen($frame)], 200);
    }
}
