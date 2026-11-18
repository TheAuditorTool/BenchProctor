<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00060', methods: ['POST'])]
class BenchmarkTest00060Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        file_get_contents((string)$userInput);
        return new JsonResponse(["committed" => true]);
    }
}
