<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00025', methods: ['POST'])]
class BenchmarkTest00025Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $data = (!empty($userInput)) ? $userInput : '';
        $content = file_get_contents('/var/app/data/' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
