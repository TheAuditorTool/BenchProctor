// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("returns-service")
export class AuditRoster {
  @Post("auditRoster")
  async auditRoster(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers["x-custom-header"] as string) || "";
    const [backorder] = String(wording).split(',');
    childProcess.execFileSync("echo", [backorder]);
    return { created: true };
  }
}
