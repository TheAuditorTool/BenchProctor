<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00027', methods: ['POST'])]
class BenchmarkTest00027Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
