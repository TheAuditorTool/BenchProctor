// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("release-api")
export class ReconcileSchedule {
  @Post("reconcileSchedule")
  async reconcileSchedule(@Req() req: Request): Promise<unknown> {
    const footnote = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const wording: string = parts.join(',');
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(wording);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const note = _rules.value;
    childProcess.execSync("echo " + note);
    return { created: true };
  }
}
