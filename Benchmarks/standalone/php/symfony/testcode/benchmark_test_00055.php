<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00055', methods: ['POST'])]
class BenchmarkTest00055Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $data = ($userInput !== null) ? $userInput : '';
        $pipes = [];
        proc_open(['echo', (string)$data], [], $pipes);
        return new JsonResponse(["committed" => true]);
    }
}
