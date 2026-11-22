<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00035Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $checkedPath = '/var/app/data/' . basename($data);
        unlink((string)$checkedPath);
        return response()->json(['ok' => 1]);
    }
}
