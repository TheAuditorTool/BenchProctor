// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("redaction-service")
export class RotateBundle {
  @Post("rotateBundle")
  async rotateBundle(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.referer as string) || "";
    const dossier = phrase != null ? phrase : '';
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + dossier + "'");
    return { created: true };
  }
}
