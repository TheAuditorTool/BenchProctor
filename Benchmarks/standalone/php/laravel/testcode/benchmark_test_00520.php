<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00520Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = vsprintf('%1$s', [$userInput]);
        $processed = \Parsedown::instance()->setSafeMode(true)->text($data);
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
