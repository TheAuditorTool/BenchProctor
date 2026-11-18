// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("upload-gateway")
export class VerifyReceipt {
  @Post("verifyReceipt")
  async verifyReceipt(@Req() req: Request): Promise<unknown> {
    const notice = process.env.MEDIA_INPUT_0045 || "";
    const parts: string[] = [];
    for (const token of String(notice).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(rendition) } });
    return { created: true };
  }
}
