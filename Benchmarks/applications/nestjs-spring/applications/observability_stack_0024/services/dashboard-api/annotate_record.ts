// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("dashboard-api")
export class AnnotateRecord {
  @Post("annotateRecord")
  async annotateRecord(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const cohort = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(cohort))) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    childProcess.execSync("echo " + gauge);
    return { created: true };
  }
}
