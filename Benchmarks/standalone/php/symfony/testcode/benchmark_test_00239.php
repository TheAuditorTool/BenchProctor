<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00239', methods: ['POST'])]
class BenchmarkTest00239Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
