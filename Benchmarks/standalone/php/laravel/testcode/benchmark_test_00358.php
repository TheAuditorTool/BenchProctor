<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00358Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = json_decode($userInput, true)['value'] ?? '';
        $processed = \Parsedown::instance()->setSafeMode(true)->text($data);
        $stream = function () use ($processed) {
            echo '<div class="comment">' . $processed . '</div>';
        };
        return response()->stream($stream, 200, ['Content-Type' => 'text/html']);
    }
}
