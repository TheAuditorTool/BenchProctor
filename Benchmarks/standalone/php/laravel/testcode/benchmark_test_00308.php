<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00308Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return response()->json(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        file_get_contents((string)$targetUrl);
        return response()->json(['ok' => 1]);
    }
}
