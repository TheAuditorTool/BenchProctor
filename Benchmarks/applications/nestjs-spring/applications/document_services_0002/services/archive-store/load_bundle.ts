// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import { IsString, Matches, validateSync } from "class-validator";

@Controller("archive-store")
export class LoadBundle {
  @Post("loadBundle")
  async loadBundle(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers["user-agent"] as string) || "";
    const addendum = wording != null ? wording : '';
    class PayloadRules {
      @IsString()
      @Matches(/^[a-zA-Z0-9 _.%\-]+$/)
      value!: string;
    }
    const _rules = new PayloadRules();
    _rules.value = String(addendum);
    const _violations = validateSync(_rules);
    if (_violations.length > 0) { throw new BadRequestException({error:"invalid"}); }
    const dossier = _rules.value;
    childProcess.exec("echo " + dossier, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
