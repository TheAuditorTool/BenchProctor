// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("editorial-workflow")
export class AuditLedger {
  @Post("auditLedger")
  async auditLedger(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body as string) || "";
    const tokens = String(synopsis).split(',').filter((t) => t.length > 0);
    const byline = tokens.join(' ');
    childProcess.spawn("echo " + byline, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
