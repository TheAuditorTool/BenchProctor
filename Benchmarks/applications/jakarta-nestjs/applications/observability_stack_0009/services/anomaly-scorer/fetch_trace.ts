// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("anomaly-scorer")
export class FetchTrace {
  @Post("fetchTrace")
  async fetchTrace(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["x-custom-header"] as string) || "";
    const [gauge] = String(summary).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(gauge)) { throw new ForbiddenException({error:'forbidden'}); }
    const cohort = gauge;
    childProcess.execSync("echo " + cohort);
    return { created: true };
  }
}
