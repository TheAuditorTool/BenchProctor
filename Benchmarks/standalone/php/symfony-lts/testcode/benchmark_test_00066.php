<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00066', methods: ['POST'])]
class BenchmarkTest00066Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        unlink('/var/app/data/' . $data);
        return new JsonResponse(["committed" => true]);
    }
}
