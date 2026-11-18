<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00573', methods: ['POST'])]
class BenchmarkTest00573Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $data = vsprintf('%1$s', [$userInput]);
        unlink('/var/app/data/' . $data);
        return new JsonResponse(["committed" => true]);
    }
}
