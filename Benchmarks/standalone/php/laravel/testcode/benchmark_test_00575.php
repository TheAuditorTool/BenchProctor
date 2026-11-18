<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00575Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        session(['data' => (string) $data]);
        return response()->json(['ok' => 1]);
    }
}
