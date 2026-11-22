<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00326Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = "{$userInput}";
        return response('', 302)->header('Location', (string)$data);
    }
}
