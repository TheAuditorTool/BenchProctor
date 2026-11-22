// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payments-api")
export class EnrichWallet {
  @Post("enrichWallet")
  async enrichWallet(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    const _raw = footnote;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(remittance)) { throw new ForbiddenException({error:'forbidden'}); }
    const disbursement = remittance;
    childProcess.execSync("echo " + disbursement);
    return { created: true };
  }
}
