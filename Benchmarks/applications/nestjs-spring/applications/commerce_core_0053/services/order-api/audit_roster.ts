// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("order-api")
export class AuditRoster {
  @Post("auditRoster")
  async auditRoster(@Req() req: Request): Promise<unknown> {
    const memo = (req.body.payload as string) || "";
    const tokens = String(memo).split(',').filter((t) => t.length > 0);
    const voucher = tokens.join(' ');
    childProcess.execSync("echo " + voucher);
    return { created: true };
  }
}
