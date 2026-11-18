<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00212Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        return response('<div>' . $userInput . '</div>')->header('Content-Type', 'text/html');
    }
}
