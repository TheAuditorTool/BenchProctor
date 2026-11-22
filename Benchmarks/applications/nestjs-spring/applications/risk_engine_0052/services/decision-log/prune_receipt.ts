// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("decision-log")
export class PruneReceipt {
  @Post("pruneReceipt")
  async pruneReceipt(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers["user-agent"] as string) || "";
    const verdict = memo != null ? memo : '';
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(verdict);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const grievance = _rules.value;
    childProcess.exec("echo " + grievance, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
