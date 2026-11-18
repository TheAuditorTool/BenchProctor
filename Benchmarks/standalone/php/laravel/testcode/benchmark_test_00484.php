<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00484Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Forwarded-For', '');
        file_put_contents('/var/uploads/' . $userInput, 'data');
        return response()->json(['ok' => 1]);
    }
}
