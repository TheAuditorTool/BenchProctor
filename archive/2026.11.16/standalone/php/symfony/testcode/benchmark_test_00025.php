<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00025', methods: ['POST'])]
class BenchmarkTest00025Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        [$data] = [$userInput, 'http'];
        file_get_contents((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
