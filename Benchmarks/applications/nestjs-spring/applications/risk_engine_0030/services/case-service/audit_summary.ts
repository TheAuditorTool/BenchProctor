// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("case-service")
export class AuditSummary {
  @Post("auditSummary")
  async auditSummary(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const grievance = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(grievance))) { throw new BadRequestException({error:"invalid"}); }
    const verdict = grievance;
    childProcess.execSync("echo " + verdict);
    return { created: true };
  }
}
