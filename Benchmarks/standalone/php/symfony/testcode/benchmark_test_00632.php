<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00632', methods: ['POST'])]
class BenchmarkTest00632Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $data = sprintf('%s', $userInput);
        $pipes = [];
        proc_open(['echo', (string)$data], [], $pipes);
        return new JsonResponse(["committed" => true]);
    }
}
