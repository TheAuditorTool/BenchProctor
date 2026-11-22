// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("knowledge-index")
export class ReconcileReceipt {
  @Post("reconcileReceipt")
  async reconcileReceipt(@Req() req: Request): Promise<unknown> {
    const blurb = (req.headers["x-custom-header"] as string) || "";
    const parts: string[] = [];
    for (const token of String(blurb).split(',')) { parts.push(token); }
    const inquiry: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    childProcess.execSync("echo " + grievance);
    return { created: true };
  }
}
