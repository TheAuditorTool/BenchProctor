<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00162', methods: ['POST'])]
class BenchmarkTest00162Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = ($userInput !== null) ? $userInput : '';
        ini_set('yaml.decode_php', '1');
        $document = yaml_parse((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
