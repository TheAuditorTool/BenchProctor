<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00030Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $pipes = [];
        $snippet = proc_open([PHP_BINARY, '-r', (string)$data], [1 => ['pipe', 'w']], $pipes);
        $result = stream_get_contents($pipes[1]);
        proc_close($snippet);
        return response()->json(['ok' => 1]);
    }
}
