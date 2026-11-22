<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00292Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $outbound = new \GuzzleHttp\Psr7\Request('GET', (string)$userInput);
        $http = new \GuzzleHttp\Client(['timeout' => 5]);
        $upstream = $http->send($outbound);
        return response()->json(['ok' => 1]);
    }
}
