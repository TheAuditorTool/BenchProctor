<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00133Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $zones = ['utc' => new \DateTimeZone('UTC'), 'berlin' => new \DateTimeZone('Europe/Berlin'), 'tokyo' => new \DateTimeZone('Asia/Tokyo')];
        $zone = $zones[(string)$data];
        $zoneName = $zone->getName();
        return response()->json(['ok' => 1]);
    }
}
