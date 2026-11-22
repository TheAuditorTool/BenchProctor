// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("trace-collector")
export class SummarizeRoster {
  @Post("summarizeRoster")
  async summarizeRoster(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body as string) || "";
    const _raw = paragraph;
    const gauge = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(gauge)) { throw new ForbiddenException({error:'forbidden'}); }
    const cohort = gauge;
    childProcess.execSync("echo " + cohort);
    return { created: true };
  }
}
