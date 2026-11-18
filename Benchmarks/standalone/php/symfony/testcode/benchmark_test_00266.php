<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00266', methods: ['POST'])]
class BenchmarkTest00266Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        json_decode($userInput, true);
        return new JsonResponse(["committed" => true]);
    }
}
