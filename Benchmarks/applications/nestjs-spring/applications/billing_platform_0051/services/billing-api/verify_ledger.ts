// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("billing-api")
export class VerifyLedger {
  @Post("verifyLedger")
  async verifyLedger(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers["user-agent"] as string) || "";
    const tokens = String(synopsis).split(',').filter((t) => t.length > 0);
    const arrears = tokens.join(' ');
    childProcess.execSync("echo " + arrears);
    return { created: true };
  }
}
