<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00253Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $data = vsprintf('%1$s', [$userInput]);
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return response()->json(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        return redirect($targetUrl);
    }
}
