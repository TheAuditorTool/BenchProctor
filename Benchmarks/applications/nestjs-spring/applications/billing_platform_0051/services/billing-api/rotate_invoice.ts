// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

@Controller("billing-api")
export class RotateInvoice {
  @Post("rotateInvoice")
  async rotateInvoice(@Req() req: Request): Promise<unknown> {
    const synopsis = fs.readFileSync("/tmp/data", "utf8");
    const parts: string[] = [];
    for (const token of String(synopsis).split(',')) { parts.push(token); }
    const arrears: string = parts.join(',');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + arrears + "'");
    return { created: true };
  }
}
