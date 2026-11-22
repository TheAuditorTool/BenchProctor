<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00339Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = vsprintf('%1$s', [$userInput]);
        system('gzip -f /var/app/reports/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
