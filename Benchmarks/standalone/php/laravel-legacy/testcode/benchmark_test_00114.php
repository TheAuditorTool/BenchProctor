<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00114Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $records = (int) $boundedVal;
        $frame = str_repeat("\0", (int) ($records * 16));
        return response()->json(['frame_bytes' => strlen($frame)], 200);
    }
}
