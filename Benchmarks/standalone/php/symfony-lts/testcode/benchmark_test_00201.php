<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\ORM\EntityManagerInterface;

#[Route('/BenchmarkTest00201', methods: ['POST'])]
class BenchmarkTest00201Controller
{
    public function __invoke(EntityManagerInterface $em)
    {
        $userInput = getenv('APP_VALUE') ?: '';
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $em->getRepository(\App\Entity\User::class)->find((int)$data);
        return new JsonResponse(["committed" => true]);
    }
}
