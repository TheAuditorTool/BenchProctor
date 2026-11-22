<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00046Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $_coerced = (float)$userInput;
        $processed = $_coerced;
        $users = simplexml_load_file('/var/app/data/users.xml');
        $matches = $users->xpath("//user[@name='" . $processed . "']");
        return response()->json(['ok' => 1]);
    }
}
