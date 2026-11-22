// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payout-service")
export class CollectManifest {
  @Post("collectManifest")
  async collectManifest(@Req() req: Request): Promise<unknown> {
    const memo = (req.body as string) || "";
    const [ledger] = String(memo).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(ledger)) { throw new ForbiddenException({error:'forbidden'}); }
    const remittance = ledger;
    childProcess.spawn("echo " + remittance, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
