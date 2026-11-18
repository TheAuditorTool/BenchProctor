<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00661Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $processed = \Parsedown::instance()->setSafeMode(true)->text($data);
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
