// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("trace-collector")
export class VerifyReport {
  @Post("verifyReport")
  async verifyReport(@Req() req: Request): Promise<unknown> {
    const caption = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const cohort: string = parts.join(',');
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(cohort));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const gauge = _parsed.data;
    childProcess.execSync("echo " + gauge);
    return { created: true };
  }
}
