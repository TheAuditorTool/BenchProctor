<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00029Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = (!empty($userInput)) ? $userInput : '';
        return redirect($data);
    }
}
