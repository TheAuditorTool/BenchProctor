// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("billing-api")
export class PruneRecord {
  @Post("pruneRecord")
  async pruneRecord(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const tokens = String(remark).split(',').filter((t) => t.length > 0);
    const remittance = tokens.join(' ');
    childProcess.execFileSync("echo", [remittance]);
    return { created: true };
  }
}
