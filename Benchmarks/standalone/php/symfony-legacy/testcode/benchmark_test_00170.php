<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00170', methods: ['POST'])]
class BenchmarkTest00170Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $data = "{$userInput}";
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
