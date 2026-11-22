<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00149', methods: ['POST'])]
class BenchmarkTest00149Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        [$data] = [$userInput, 'http'];
        ini_set('yaml.decode_php', '1');
        $document = yaml_parse((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
