<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00042', methods: ['POST'])]
class BenchmarkTest00042Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $data = sprintf('%s', $userInput);
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
