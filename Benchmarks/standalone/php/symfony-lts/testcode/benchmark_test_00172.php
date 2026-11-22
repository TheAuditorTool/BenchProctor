<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00172', methods: ['POST'])]
class BenchmarkTest00172Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $session = $request->getSession();
        $session->replace(array_merge($session->all(), ['data' => (string) $data, 'data_updated_at' => time()]));
        return new JsonResponse(["committed" => true]);
    }
}
