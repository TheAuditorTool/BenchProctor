<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00154', methods: ['POST'])]
class BenchmarkTest00154Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = ($userInput !== null) ? $userInput : '';
        $reader = new \XMLReader();
        $reader->XML((string)$data, null, LIBXML_NOENT | LIBXML_DTDLOAD);
        $name = '';
        while ($reader->read()) {
            if ($reader->nodeType === \XMLReader::ELEMENT && $reader->name === 'name') { $name = $reader->readString(); }
        }
        return new JsonResponse(["committed" => true]);
    }
}
