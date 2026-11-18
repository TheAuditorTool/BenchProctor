<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\ORM\EntityManagerInterface;

#[Route('/BenchmarkTest00566', methods: ['POST'])]
class BenchmarkTest00566Controller
{
    public function __invoke(EntityManagerInterface $em)
    {
        $userInput = file_get_contents('/tmp/data');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $em->getRepository(\App\Entity\User::class)->find((int)$data);
        return new JsonResponse(["committed" => true]);
    }
}
