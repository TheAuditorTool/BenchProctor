<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00131Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = sprintf('%s', $userInput);
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return response()->json(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        $errno = 0; $errstr = '';
        fsockopen((string)$targetUrl, 80, $errno, $errstr, 30);
        return response()->json(['ok' => 1]);
    }
}
