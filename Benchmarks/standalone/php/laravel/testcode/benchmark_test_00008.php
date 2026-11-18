<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00008Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        unserialize($data);
        return response()->json(['ok' => 1]);
    }
}
