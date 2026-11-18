<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00289Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        simplexml_load_string($data, 'SimpleXMLElement', LIBXML_NONET);
        return response()->json(['ok' => 1]);
    }
}
