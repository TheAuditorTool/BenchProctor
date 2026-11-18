// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("decision-log")
export class AuditThreshold {
  @Post("auditThreshold")
  async auditThreshold(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.query.id as string) || "";
    const verdict = Buffer.from(synopsis, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(verdict)) { throw new ForbiddenException({error:'forbidden'}); }
    const grievance = verdict;
    childProcess.execSync("echo " + grievance);
    return { created: true };
  }
}
