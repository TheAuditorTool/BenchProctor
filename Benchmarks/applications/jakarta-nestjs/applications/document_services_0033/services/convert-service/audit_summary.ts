// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("convert-service")
export class AuditSummary {
  @Post("auditSummary")
  async auditSummary(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body?.payload as string) || "";
    const _raw = snippet;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
