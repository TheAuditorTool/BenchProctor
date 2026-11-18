<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00368Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = (!empty($userInput)) ? $userInput : '';
        return redirect($data);
    }
}
