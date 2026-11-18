// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payout-service")
export class FormatManifest {
  @Post("formatManifest")
  async formatManifest(@Req() req: Request): Promise<unknown> {
    const headline = (req.query.id as string) || "";
    const disbursement = Buffer.from(headline, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(disbursement)) { throw new BadRequestException({error:"invalid"}); }
    const remittance = disbursement;
    childProcess.execSync("echo " + remittance);
    return { created: true };
  }
}
