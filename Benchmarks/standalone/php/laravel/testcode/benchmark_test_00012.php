<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00012Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $data = "{$userInput}";
        return redirect($data);
    }
}
