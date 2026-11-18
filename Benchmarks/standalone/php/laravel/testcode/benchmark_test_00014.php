<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00014Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        return response('<div>' . $data . '</div>')->header('Content-Type', 'text/html');
    }
}
