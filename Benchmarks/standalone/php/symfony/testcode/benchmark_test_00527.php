<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00527', methods: ['POST'])]
class BenchmarkTest00527Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('User-Agent', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        file_put_contents('/var/uploads/' . $data, 'data');
        return new JsonResponse(["committed" => true]);
    }
}
