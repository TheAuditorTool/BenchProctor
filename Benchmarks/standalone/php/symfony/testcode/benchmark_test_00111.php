<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00111', methods: ['POST'])]
class BenchmarkTest00111Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = "{$userInput}";
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
