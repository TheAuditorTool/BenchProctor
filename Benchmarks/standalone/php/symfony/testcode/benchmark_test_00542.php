<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00542', methods: ['POST'])]
class BenchmarkTest00542Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
