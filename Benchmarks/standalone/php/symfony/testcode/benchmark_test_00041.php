<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00041', methods: ['POST'])]
class BenchmarkTest00041Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query->get('id', '');
        $data = str_replace("\0", '', $userInput);
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
