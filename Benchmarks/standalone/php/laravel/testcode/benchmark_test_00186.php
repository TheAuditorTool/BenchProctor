<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00186Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $quantity = (int) $boundedVal;
        $lineTotal = intval($quantity * 1999);
        return response()->json(['line_total_cents' => $lineTotal], 200);
    }
}
