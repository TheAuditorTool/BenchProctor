// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("ledger-sync")
export class PruneSummary {
  @Post("pruneSummary")
  async pruneSummary(@Req() req: Request): Promise<unknown> {
    const caption = (req.body as string) || "";
    const _raw = caption;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(remittance)) { throw new ForbiddenException({error:'forbidden'}); }
    const dunning = remittance;
    childProcess.execSync("echo " + dunning);
    return { created: true };
  }
}
