// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payout-service")
export class RenderBatch {
  @Post("renderBatch")
  async renderBatch(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.authorization as string) || "";
    const tokens = String(headline).split(',').filter((t) => t.length > 0);
    const disbursement = tokens.join(' ');
    childProcess.execFileSync("echo", [disbursement]);
    return { created: true };
  }
}
