<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00005Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $_prefix = strtolower(substr($userInput, 0, 1));
        $data = '';
        switch ($_prefix) {
            case 'h': $data = strtolower($userInput); break;
            case 'f': $data = strtoupper($userInput); break;
            default: $data = trim($userInput); break;
        }
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return response()->json(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        $errno = 0; $errstr = '';
        fsockopen((string)$targetUrl, 80, $errno, $errstr, 30);
        return response()->json(['ok' => 1]);
    }
}
