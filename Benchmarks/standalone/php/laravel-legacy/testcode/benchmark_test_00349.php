<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00349Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $data = str_replace("\0", '', $userInput);
        $scheme = strtolower((string) parse_url($data, PHP_URL_SCHEME));
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!in_array($scheme, ['http', 'https'], true) || preg_match('/[\x00-\x20\\\\]/', (string) $data) || !preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return response()->json(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        $errno = 0; $errstr = '';
        fsockopen((string) parse_url((string)$targetUrl, PHP_URL_HOST), 80, $errno, $errstr, 30);
        return response()->json(['ok' => 1]);
    }
}
