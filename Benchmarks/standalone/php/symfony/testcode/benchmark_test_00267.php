<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00267', methods: ['POST'])]
class BenchmarkTest00267Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
