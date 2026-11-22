<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00118', methods: ['POST'])]
class BenchmarkTest00118Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $data = ($userInput !== null) ? $userInput : '';
        $_coerced = (float)$data;
        $processed = $_coerced;
        $pipes = [];
        $snippet = proc_open([PHP_BINARY, '-r', (string)$processed], [1 => ['pipe', 'w']], $pipes);
        $result = stream_get_contents($pipes[1]);
        proc_close($snippet);
        return new JsonResponse(["committed" => true]);
    }
}
