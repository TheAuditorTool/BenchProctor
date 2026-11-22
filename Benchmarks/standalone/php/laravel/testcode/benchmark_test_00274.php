<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00274Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $users = simplexml_load_file('/var/app/data/users.xml');
        $matches = $users->xpath("//user[@name='" . $userInput . "']");
        return response()->json(['ok' => 1]);
    }
}
