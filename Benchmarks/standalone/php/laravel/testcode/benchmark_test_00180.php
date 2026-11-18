<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00180Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = json_decode($userInput, true)['value'] ?? '';
        return response('<div>' . $data . '</div>')->header('Content-Type', 'text/html');
    }
}
