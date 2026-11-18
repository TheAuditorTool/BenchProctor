<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00105Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = str_replace("\0", '', $userInput);
        return response(e($data))->header('Content-Type', 'text/html');
    }
}
