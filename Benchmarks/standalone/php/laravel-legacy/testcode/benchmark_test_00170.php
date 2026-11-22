<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00170Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $_coerced = (float)$data;
        $processed = $_coerced;
        $pipes = [];
        $snippet = proc_open([PHP_BINARY, '-r', (string)$processed], [1 => ['pipe', 'w']], $pipes);
        $result = stream_get_contents($pipes[1]);
        proc_close($snippet);
        return response()->json(['ok' => 1]);
    }
}
