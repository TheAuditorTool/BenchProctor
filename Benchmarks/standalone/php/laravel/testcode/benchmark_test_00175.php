<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00175Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $zones = ['utc' => new \DateTimeZone('UTC'), 'berlin' => new \DateTimeZone('Europe/Berlin'), 'tokyo' => new \DateTimeZone('Asia/Tokyo')];
        $zone = $zones[(string)$data] ?? null;
        if ($zone === null) { return response()->json(["error" => "not found"], 404); }
        $zoneName = $zone->getName();
        return response()->json(['ok' => 1]);
    }
}
