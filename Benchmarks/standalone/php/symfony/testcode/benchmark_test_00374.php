<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00374', methods: ['POST'])]
class BenchmarkTest00374Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
