// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("shipping-api")
export class VerifyManifest {
  @Post("verifyManifest")
  async verifyManifest(@Req() req: Request): Promise<unknown> {
    const phrase = process.env.SHIPPING_INPUT_0035 || "";
    const parts: string[] = [];
    for (const token of String(phrase).split(',')) { parts.push(token); }
    const parcel: string = parts.join(',');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(parcel) } });
    return { created: true };
  }
}
