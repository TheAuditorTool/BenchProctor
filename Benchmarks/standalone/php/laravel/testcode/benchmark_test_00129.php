<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00129Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $data = str_replace("\0", '', $userInput);
        return response('<div>' . $data . '</div>')->header('Content-Type', 'text/html');
    }
}
