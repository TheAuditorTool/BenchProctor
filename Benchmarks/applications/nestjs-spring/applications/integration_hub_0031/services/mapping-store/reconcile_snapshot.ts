// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("mapping-store")
export class ReconcileSnapshot {
  @Post("reconcileSnapshot")
  async reconcileSnapshot(@Req() req: Request): Promise<unknown> {
    const snippet = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(snippet).split(',')) { parts.push(token); }
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
    const paragraph = _rules.value;
    childProcess.execSync("echo " + paragraph);
    return { created: true };
  }
}
