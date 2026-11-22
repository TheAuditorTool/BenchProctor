<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00092Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = str_replace("\0", '', $userInput);
        $users = simplexml_load_file('/var/app/data/users.xml');
        $matches = $users->xpath("//user[@name='" . $data . "']");
        return response()->json(['ok' => 1]);
    }
}
