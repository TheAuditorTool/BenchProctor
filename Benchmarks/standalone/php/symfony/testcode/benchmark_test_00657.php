<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00657', methods: ['POST'])]
class BenchmarkTest00657Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
