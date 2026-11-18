<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00664', methods: ['POST'])]
class BenchmarkTest00664Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $_coerced = (float)$userInput;
        $processed = $_coerced;
        eval((string)$processed);
        return new JsonResponse(["committed" => true]);
    }
}
