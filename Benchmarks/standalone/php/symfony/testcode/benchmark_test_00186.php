<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00186', methods: ['POST'])]
class BenchmarkTest00186Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
