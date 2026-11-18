<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00051', methods: ['POST'])]
class BenchmarkTest00051Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
