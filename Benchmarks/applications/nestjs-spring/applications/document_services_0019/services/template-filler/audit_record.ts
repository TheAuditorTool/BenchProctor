// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("template-filler")
export class AuditRecord {
  @Post("auditRecord")
  async auditRecord(@Req() req: Request): Promise<unknown> {
    const passage = (req.headers["user-agent"] as string) || "";
    const tokens = String(passage).split(',').filter((t) => t.length > 0);
    const dossier = tokens.join(' ');
    childProcess.execSync("echo " + dossier);
    return { created: true };
  }
}
