// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payout-service")
export class CompactIndex {
  @Post("compactIndex")
  async compactIndex(@Req() req: Request): Promise<unknown> {
    const headline = (req.body as string) || "";
    const disbursement = Buffer.from(headline, "base64").toString();
    childProcess.execSync("echo " + disbursement);
    return { created: true };
  }
}
