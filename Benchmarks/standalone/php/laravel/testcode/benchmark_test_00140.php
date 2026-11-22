<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00140Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        return response('', 302)->header('Location', (string)$data);
    }
}
