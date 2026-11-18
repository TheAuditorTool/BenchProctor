<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00074', methods: ['POST'])]
class BenchmarkTest00074Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $_coerced = in_array(strtolower((string)$data), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        $request->getSession()->set('data', (string) $parsedBool);
        return new JsonResponse(["committed" => true]);
    }
}
