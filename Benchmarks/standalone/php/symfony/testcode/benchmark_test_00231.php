<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00231', methods: ['POST'])]
class BenchmarkTest00231Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = str_replace("\0", '', $userInput);
        $request->getSession()->set('data', (string) $data);
        return new JsonResponse(["committed" => true]);
    }
}
