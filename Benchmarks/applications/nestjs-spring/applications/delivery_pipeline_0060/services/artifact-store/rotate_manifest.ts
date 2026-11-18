// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("artifact-store")
export class RotateManifest {
  @Post("rotateManifest")
  async rotateManifest(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.authorization as string) || "";
    const tokens = String(wording).split(',').filter((t) => t.length > 0);
    const remark = tokens.join(' ');
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.user.findUnique({ where: { id: Number(remark) } });
    return { created: true };
  }
}
