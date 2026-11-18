<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00505Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        file_put_contents('/var/uploads/' . $data, 'data');
        return response()->json(['ok' => 1]);
    }
}
