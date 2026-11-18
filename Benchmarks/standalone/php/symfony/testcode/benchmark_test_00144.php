<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00144', methods: ['POST'])]
class BenchmarkTest00144Controller
{
    public function __invoke()
    {
        $userInput = (new \Redis())->get('user_data');
        unserialize($userInput);
        return new JsonResponse(["committed" => true]);
    }
}
