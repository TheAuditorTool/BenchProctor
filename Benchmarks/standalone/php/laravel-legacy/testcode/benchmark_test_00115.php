<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00115Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = mb_convert_encoding($userInput, 'UTF-8');
        file_put_contents('/var/uploads/' . $data, 'data');
        return response()->json(['ok' => 1]);
    }
}
