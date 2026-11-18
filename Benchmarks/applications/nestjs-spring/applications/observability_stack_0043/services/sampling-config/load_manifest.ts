// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("sampling-config")
export class LoadManifest {
  @Post("loadManifest")
  async loadManifest(@Req() req: Request): Promise<unknown> {
    const note = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(note).split(',')) { parts.push(token); }
    const gauge: string = parts.join(',');
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(gauge);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const cohort = _rules.value;
    childProcess.execSync("echo " + cohort);
    return { created: true };
  }
}
