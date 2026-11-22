<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00083Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $data = sprintf('%s', $userInput);
        $zones = ['utc' => new \DateTimeZone('UTC'), 'berlin' => new \DateTimeZone('Europe/Berlin'), 'tokyo' => new \DateTimeZone('Asia/Tokyo')];
        $zone = $zones[(string)$data];
        $zoneName = $zone->getName();
        return response()->json(['ok' => 1]);
    }
}
