<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00224', methods: ['POST'])]
class BenchmarkTest00224Controller
{
    public function __invoke()
    {
        $userInput = (new \Redis())->get('user_data');
        $data = "{$userInput}";
        file_get_contents((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
