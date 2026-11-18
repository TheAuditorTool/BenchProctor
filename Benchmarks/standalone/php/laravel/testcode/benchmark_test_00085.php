<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00085Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        [$data] = [$userInput, 'http'];
        $processed = (new \HTMLPurifier())->purify($data);
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
