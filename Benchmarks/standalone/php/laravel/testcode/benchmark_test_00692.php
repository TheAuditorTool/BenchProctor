<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00692Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $data = ($userInput !== null) ? $userInput : '';
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        $resolved = gethostbyname($host);
        if (preg_match('#^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)#', $resolved)) { return response()->json(['error' => 'private range blocked'], 403); }
        $targetUrl = $data;
        file_get_contents((string)$targetUrl);
        return response()->json(['ok' => 1]);
    }
}
