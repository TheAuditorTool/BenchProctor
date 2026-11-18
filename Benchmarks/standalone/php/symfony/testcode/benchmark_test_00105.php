<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00105', methods: ['POST'])]
class BenchmarkTest00105Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
