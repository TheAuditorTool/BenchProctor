<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00327', methods: ['POST'])]
class BenchmarkTest00327Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $data = sprintf('%s', $userInput);
        $request->getSession()->set('data', (string) $data);
        return new JsonResponse(["committed" => true]);
    }
}
