// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("payments-api")
export class AuditThreshold {
  @Post("auditThreshold")
  async auditThreshold(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers["user-agent"] as string) || "";
    let ledger;
    try { ledger = JSON.parse(subject).value || subject; }
    catch (e) { ledger = subject; }
    JSON.parse(ledger);
    return { created: true };
  }
}
