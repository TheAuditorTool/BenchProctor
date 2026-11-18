// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("redaction-service")
export class SummarizeRecord {
  @Post("summarizeRecord")
  async summarizeRecord(@Req() req: Request): Promise<unknown> {
    const passage = (req.body.payload as string) || "";
    const _raw = passage;
    const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(dossier);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const addendum = _rules.value;
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
