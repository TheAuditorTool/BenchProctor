<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00625Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = vsprintf('%1$s', [$userInput]);
        unlink('/var/app/data/' . $data);
        return response()->json(['ok' => 1]);
    }
}
