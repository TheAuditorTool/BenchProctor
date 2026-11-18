// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("config-service")
export class AuditHeader {
  @Post("auditHeader")
  async auditHeader(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const persona = handshake;
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
