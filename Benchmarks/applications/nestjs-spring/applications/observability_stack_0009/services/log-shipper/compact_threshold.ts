// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("log-shipper")
export class CompactThreshold {
  @Post("compactThreshold")
  async compactThreshold(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const gauge = tokens.join(' ');
    childProcess.execFileSync("echo", [gauge]);
    return { created: true };
  }
}
