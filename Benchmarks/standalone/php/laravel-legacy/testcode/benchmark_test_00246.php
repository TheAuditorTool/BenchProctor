<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00246Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = sprintf('%s', $userInput);
        return \Illuminate\Support\Facades\Redirect::away((string)$data);
    }
}
