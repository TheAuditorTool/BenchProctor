// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("profile-api")
export class AuditDevice {
  @Post("auditDevice")
  async auditDevice(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.cookies?.session_token as string) || "";
    const _raw = paragraph;
    const persona = (_raw && _raw.length > 0) ? _raw : 'default';
    const resolved = path.resolve("/var/app/data", persona);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const blurb = resolved;
    const fileContent = fs.readFileSync(blurb, "utf8");
    return fileContent;
  }
}
