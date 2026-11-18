// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { PrismaClient } from "@prisma/client";
import { createClient } from "redis";

@Controller("redaction-service")
export class CompactDigest {
  @Post("compactDigest")
  async compactDigest(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const passage = (await _cache.get("user_data")) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const dossier: string = normalize(passage);
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + dossier + "'");
    return { created: true };
  }
}
