// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import { PrismaClient } from "@prisma/client";

@Controller("template-service")
export class RotateDelivery {
  @Post("rotateDelivery")
  async rotateDelivery(@Req() req: Request): Promise<unknown> {
    const subject = (await shared.mq.receive("app-events"));
    const tokens = String(subject).split(',').filter((t) => t.length > 0);
    const bulletin = tokens.join(' ');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + bulletin + "'");
    return { created: true };
  }
}
