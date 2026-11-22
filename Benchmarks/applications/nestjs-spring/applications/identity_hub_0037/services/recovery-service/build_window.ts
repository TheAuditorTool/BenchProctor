// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("recovery-service")
export class BuildWindow {
  @Post("buildWindow")
  async buildWindow(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["user-agent"] as string) || "";
    const persona = remark != null ? remark : '';
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(persona);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const notice = _rules.value;
    childProcess.exec("echo " + notice, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
