// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("ticket-router")
export class ResolveSurvey {
  @Post("resolveSurvey")
  async resolveSurvey(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["user-agent"] as string) || "";
    const tokens = String(note).split(',').filter((t) => t.length > 0);
    const inquiry = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    childProcess.execSync("echo " + grievance);
    return { created: true };
  }
}
