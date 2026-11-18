<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00059Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $processed = (new \HTMLPurifier())->purify($data);
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
