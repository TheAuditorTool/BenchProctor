// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import { PrismaClient } from "@prisma/client";

@Controller("promo-service")
export class LoadWindow {
  @Post("loadWindow")
  async loadWindow(@Req() req: Request): Promise<unknown> {
    const heading = (await shared.mq.receive("app-events"));
    const tokens = String(heading).split(',').filter((t) => t.length > 0);
    const voucher = tokens.join(' ');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + voucher + "'");
    return { created: true };
  }
}
