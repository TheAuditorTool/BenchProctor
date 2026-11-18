<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00491', methods: ['POST'])]
class BenchmarkTest00491Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = str_replace("\0", '', $userInput);
        $content = file_get_contents('/var/app/data/' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
