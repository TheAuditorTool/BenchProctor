<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00250Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = str_replace("\0", '', $userInput);
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        \Illuminate\Support\Facades\Session::put(['data' => (string) $parsedBool, 'data_updated_at' => time()]);
        return response()->json(['ok' => 1]);
    }
}
