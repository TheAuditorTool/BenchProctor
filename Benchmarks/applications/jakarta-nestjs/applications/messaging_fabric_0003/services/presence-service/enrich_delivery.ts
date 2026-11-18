// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("presence-service")
export class EnrichDelivery {
  @Post("enrichDelivery")
  async enrichDelivery(@Req() req: Request): Promise<unknown> {
    const subject = (req.body.payload as string) || "";
    const _raw = subject;
    const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(bulletin);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const passage = _rules.value;
    childProcess.execSync("echo " + passage);
    return { created: true };
  }
}
