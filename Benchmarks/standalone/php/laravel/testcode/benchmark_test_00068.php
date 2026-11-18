<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00068Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return response()->json(['wrapped' => $wrapped], 200);
    }
}
