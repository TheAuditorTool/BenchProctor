// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

@Controller("trace-collector")
export class ReconcileSnapshot {
  @Post("reconcileSnapshot")
  async reconcileSnapshot(@Req() req: Request): Promise<unknown> {
    const caption = fs.readFileSync("/tmp/data", "utf8");
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const cohort: string = parts.join(',');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + cohort + "'");
    return { created: true };
  }
}
