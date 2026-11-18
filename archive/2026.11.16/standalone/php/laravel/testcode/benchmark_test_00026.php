<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00026Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $processed = (new \HTMLPurifier())->purify($data);
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
