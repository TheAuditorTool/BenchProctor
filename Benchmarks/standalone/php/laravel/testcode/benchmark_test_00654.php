<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00654Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $data = str_replace("\0", '', $userInput);
        unlink('/var/app/data/' . $data);
        return response()->json(['ok' => 1]);
    }
}
