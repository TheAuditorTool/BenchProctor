<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00148', methods: ['POST'])]
class BenchmarkTest00148Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Forwarded-For', '');
        file_put_contents('/var/uploads/' . $userInput, 'data');
        return new JsonResponse(["committed" => true]);
    }
}
