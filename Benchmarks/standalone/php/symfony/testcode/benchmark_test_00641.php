<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00641', methods: ['POST'])]
class BenchmarkTest00641Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return new JsonResponse(['wrapped' => $wrapped], 200);
    }
}
