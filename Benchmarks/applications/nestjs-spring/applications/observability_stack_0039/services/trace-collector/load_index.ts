// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("trace-collector")
export class LoadIndex {
  @Post("loadIndex")
  async loadIndex(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.authorization as string) || "";
    const tokens = String(caption).split(',').filter((t) => t.length > 0);
    const cohort = tokens.join(' ');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(cohort) } });
    return { created: true };
  }
}
