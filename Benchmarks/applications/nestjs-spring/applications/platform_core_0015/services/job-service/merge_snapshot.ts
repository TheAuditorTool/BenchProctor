// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("job-service")
export class MergeSnapshot {
  @Post("mergeSnapshot")
  async mergeSnapshot(@Req() req: Request): Promise<unknown> {
    const note = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(note).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(handshake);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const persona = _rules.value;
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
