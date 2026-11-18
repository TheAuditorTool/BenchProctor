// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";

@Controller("retry-service")
export class EnrichThreshold {
  @Post("enrichThreshold")
  async enrichThreshold(@Req() req: Request): Promise<unknown> {
    const synopsis = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(synopsis);
    const handshake: string = readInput();
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + handshake + "'");
    return { created: true };
  }
}
