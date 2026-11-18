// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("anomaly-scorer")
export class RenderReport {
  @Post("renderReport")
  async renderReport(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    const cohort = Buffer.from(caption, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(cohort)) { throw new ForbiddenException({error:'forbidden'}); }
    const gauge = cohort;
    childProcess.execSync("echo " + gauge);
    return { created: true };
  }
}
