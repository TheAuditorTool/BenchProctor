<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00339Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return response()->json(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        system('gzip -f /var/app/reports/' . (string)$allowedBin);
        return response()->json(['ok' => 1]);
    }
}
