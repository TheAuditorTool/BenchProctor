// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("audit-log")
export class AppendAudit {
  @Post("appendAudit")
  async appendAudit(@Req() req: Request): Promise<unknown> {
    const transcript = req.body.platform_payload || "";
    const resolved = path.resolve("/var/app/data", transcript);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const handshake = resolved;
    const fileContent = fs.readFileSync(handshake, "utf8");
    return fileContent;
  }
}
