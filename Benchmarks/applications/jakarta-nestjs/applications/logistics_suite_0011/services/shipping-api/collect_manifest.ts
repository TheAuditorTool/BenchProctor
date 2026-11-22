// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

@Controller("shipping-api")
export class CollectManifest {
  @Post("collectManifest")
  async collectManifest(@Req() req: Request): Promise<unknown> {
    const citation = fs.readFileSync("/tmp/data", "utf8");
    const consignment = citation != null ? citation : '';
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(consignment) } });
    return { created: true };
  }
}
