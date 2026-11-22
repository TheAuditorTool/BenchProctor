<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00110', methods: ['POST'])]
class BenchmarkTest00110Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
