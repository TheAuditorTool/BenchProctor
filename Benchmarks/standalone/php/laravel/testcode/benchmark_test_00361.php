<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00361Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = ($userInput !== null) ? $userInput : '';
        return redirect($data);
    }
}
