<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00145Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $data = sprintf('%s', $userInput);
        system('gzip -f /var/app/reports/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
