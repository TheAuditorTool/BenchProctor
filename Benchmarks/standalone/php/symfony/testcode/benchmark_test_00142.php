<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00142', methods: ['POST'])]
class BenchmarkTest00142Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
