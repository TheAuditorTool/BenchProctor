// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("fx-service")
export class MergeBundle {
  @Post("mergeBundle")
  async mergeBundle(@Req() req: Request): Promise<unknown> {
    const subject = (req.query.id as string) || "";
    const ledger = Buffer.from(subject, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(ledger)) { throw new BadRequestException({error:"invalid"}); }
    const disbursement = ledger;
    childProcess.execSync("echo " + disbursement);
    return { created: true };
  }
}
