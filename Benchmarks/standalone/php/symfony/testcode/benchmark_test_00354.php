<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00354', methods: ['POST'])]
class BenchmarkTest00354Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        mt_srand(ctype_digit((string)$data) ? (int)$data : 42);
        $token = mt_rand();
        return new JsonResponse(['token' => (string)$token], 200);
    }
}
