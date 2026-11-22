// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("editorial-workflow")
export class AnnotateThreshold {
  @Post("annotateThreshold")
  async annotateThreshold(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers["user-agent"] as string) || "";
    const byline = synopsis != null ? synopsis : '';
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(byline);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const addendum = _rules.value;
    childProcess.exec("echo " + addendum, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
