<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00016Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $outbound = new \GuzzleHttp\Psr7\Request('GET', (string)$data);
        $http = new \GuzzleHttp\Client(['timeout' => 5]);
        $upstream = $http->send($outbound);
        return response()->json(['ok' => 1]);
    }
}
