<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00524', methods: ['POST'])]
class BenchmarkTest00524Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        eval((string)$userInput);
        return new JsonResponse(["committed" => true]);
    }
}
