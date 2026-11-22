<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00037', methods: ['POST'])]
class BenchmarkTest00037Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $session = $request->getSession();
        $session->replace(array_merge($session->all(), ['data' => (string) $data, 'data_updated_at' => time()]));
        return new JsonResponse(["committed" => true]);
    }
}
