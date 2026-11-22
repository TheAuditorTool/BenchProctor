<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00127Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Host', '');
        $data = vsprintf('%1$s', [$userInput]);
        $outbound = new \GuzzleHttp\Psr7\Request('GET', (string)$data);
        $http = new \GuzzleHttp\Client(['timeout' => 5]);
        $upstream = $http->send($outbound);
        return response()->json(['ok' => 1]);
    }
}
