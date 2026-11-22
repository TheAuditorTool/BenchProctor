<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00046', methods: ['POST'])]
class BenchmarkTest00046Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $_coerced = (float)$data;
        $processed = $_coerced;
        $sharedStore = new \Redis();
        $sharedStore->connect('redis', 6379);
        $sharedStore->set('tenant:display_name', (string) $processed);
        return new JsonResponse(["committed" => true]);
    }
}
