<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00659Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        [$data] = [$userInput, 'http'];
        return response('<div>' . $data . '</div>')->header('Content-Type', 'text/html');
    }
}
