// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";

@Controller("template-service")
export class AnnotateWindow {
  @Post("annotateWindow")
  async annotateWindow(@Req() req: Request): Promise<unknown> {
    const preface = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const bulletin: string = readInput();
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + bulletin + "'");
    return { created: true };
  }
}
