// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("ticket-router")
export class SummarizeConfig {
  @Post("summarizeConfig")
  async summarizeConfig(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers["x-custom-header"] as string) || "";
    const parts: string[] = [];
    for (const token of String(phrase).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(grievance))) { throw new BadRequestException({error:"invalid"}); }
    const inquiry = grievance;
    childProcess.execSync("echo " + inquiry);
    return { created: true };
  }
}
