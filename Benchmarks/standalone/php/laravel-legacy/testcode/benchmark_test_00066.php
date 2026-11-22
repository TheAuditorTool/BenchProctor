<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00066Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        [$data] = [$userInput, 'http'];
        $processed = (new \HTMLPurifier())->purify($data);
        $stream = function () use ($processed) {
            echo '<div class="comment">' . $processed . '</div>';
        };
        return response()->stream($stream, 200, ['Content-Type' => 'text/html']);
    }
}
