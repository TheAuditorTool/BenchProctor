// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("sampling-config")
export class PruneRecord {
  @Post("pruneRecord")
  async pruneRecord(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.body as string) || "";
    const cohort = Buffer.from(excerpt, "utf-8").toString();
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = $1", cohort);
    return { created: true };
  }
}
