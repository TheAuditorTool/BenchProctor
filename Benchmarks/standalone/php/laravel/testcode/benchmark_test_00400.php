<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00400Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return response()->json(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        $errno = 0; $errstr = '';
        fsockopen((string)$targetUrl, 80, $errno, $errstr, 30);
        return response()->json(['ok' => 1]);
    }
}
