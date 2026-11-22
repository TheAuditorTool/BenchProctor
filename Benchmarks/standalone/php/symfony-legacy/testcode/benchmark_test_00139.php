<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00139', methods: ['POST'])]
class BenchmarkTest00139Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        [$data] = [$userInput, 'http'];
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
