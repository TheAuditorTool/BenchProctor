<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00223Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $response = response()->json(['ok' => 1]);
        $response->header('Set-Cookie', 'session=' . rawurlencode((string)$data) . '; Path=/; HttpOnly; SameSite=Strict');
        return $response;
    }
}
