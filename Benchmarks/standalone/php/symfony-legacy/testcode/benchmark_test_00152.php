<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00152', methods: ['POST'])]
class BenchmarkTest00152Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $pipes = [];
        $snippet = proc_open([PHP_BINARY, '-r', (string)$data], [1 => ['pipe', 'w']], $pipes);
        $result = stream_get_contents($pipes[1]);
        proc_close($snippet);
        return new JsonResponse(["committed" => true]);
    }
}
