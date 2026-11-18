// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";

@Controller("redaction-service")
export class ReconcileIndex {
  @Post("reconcileIndex")
  async reconcileIndex(@Req() req: Request): Promise<unknown> {
    const passage = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const dossier = passage != null ? passage : '';
    const _coerced = parseInt(String(dossier), 10);
    const addendum = _coerced;
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + addendum + "'");
    return { created: true };
  }
}
