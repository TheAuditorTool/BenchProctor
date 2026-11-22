<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00085Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        $data = "{$userInput}";
        $checkedPath = '/var/app/data/' . basename($data);
        $content = file_get_contents($checkedPath);
        return response()->json(['ok' => 1]);
    }
}
