// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("message-api")
export class SummarizeSchedule {
  @Post("summarizeSchedule")
  async summarizeSchedule(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const bulletin = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const snippet = bulletin;
    childProcess.execSync("echo " + snippet);
    return { created: true };
  }
}
