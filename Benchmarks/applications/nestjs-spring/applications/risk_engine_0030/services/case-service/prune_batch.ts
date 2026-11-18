// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("case-service")
export class PruneBatch {
  @Post("pruneBatch")
  async pruneBatch(@Req() req: Request): Promise<unknown> {
    const summary = (req.query.id as string) || "";
    const grievance = Buffer.from(summary, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(grievance)) { throw new BadRequestException({error:"invalid"}); }
    const verdict = grievance;
    childProcess.execSync("echo " + verdict);
    return { created: true };
  }
}
