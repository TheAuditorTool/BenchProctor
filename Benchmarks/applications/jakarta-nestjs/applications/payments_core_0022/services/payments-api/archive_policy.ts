// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payments-api")
export class ArchivePolicy {
  @Post("archivePolicy")
  async archivePolicy(@Req() req: Request): Promise<unknown> {
    const subject = (req.query.id as string) || "";
    const ledger = Buffer.from(subject, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(ledger)) { throw new ForbiddenException({error:'forbidden'}); }
    const disbursement = ledger;
    childProcess.execSync("echo " + disbursement);
    return { created: true };
  }
}
