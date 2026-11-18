<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00419Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = ($userInput !== null) ? $userInput : '';
        return redirect($data);
    }
}
