<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00010Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        $pipes = [];
        $snippet = proc_open([PHP_BINARY, '-r', (string)$parsedBool], [1 => ['pipe', 'w']], $pipes);
        $result = stream_get_contents($pipes[1]);
        proc_close($snippet);
        return response()->json(['ok' => 1]);
    }
}
