// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { PrismaClient } from "@prisma/client";

@Controller("upload-gateway")
export class AuditConfig {
  @Post("auditConfig")
  async auditConfig(@Req() req: Request): Promise<unknown> {
    const transcript = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
    let rendition;
    try { rendition = JSON.parse(transcript).value || ""; }
    catch (e) { rendition = String(transcript); }
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + rendition + "'");
    return { created: true };
  }
}
