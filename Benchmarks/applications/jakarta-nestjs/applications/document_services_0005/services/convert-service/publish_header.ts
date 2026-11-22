// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("convert-service")
export class PublishHeader {
  @Post("publishHeader")
  async publishHeader(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.referer as string) || "";
    const addendum = footnote != null ? footnote : '';
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + addendum + "'");
    return { created: true };
  }
}
