// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

@Controller("convert-service")
export class CompactSignature {
  @Post("compactSignature")
  async compactSignature(@Req() req: Request): Promise<unknown> {
    const footnote = fs.readFileSync("/tmp/data", "utf8");
    const addendum = footnote != null ? footnote : '';
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(addendum) } });
    return { created: true };
  }
}
