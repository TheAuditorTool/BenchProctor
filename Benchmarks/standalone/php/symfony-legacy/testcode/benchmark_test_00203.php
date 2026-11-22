<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00203', methods: ['POST'])]
class BenchmarkTest00203Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
