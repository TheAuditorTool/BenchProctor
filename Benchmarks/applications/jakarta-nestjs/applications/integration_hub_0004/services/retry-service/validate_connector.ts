// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

@Controller("retry-service")
export class ValidateConnector {
  @Post("validateConnector")
  async validateConnector(@Req() req: Request): Promise<unknown> {
    const summary = fs.readFileSync("/tmp/data", "utf8");
    const handshake = summary != null ? summary : '';
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(handshake) } });
    return { created: true };
  }
}
