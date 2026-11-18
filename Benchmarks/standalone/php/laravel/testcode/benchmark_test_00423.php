<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00423Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        return response('<div>' . $data . '</div>')->header('Content-Type', 'text/html');
    }
}
