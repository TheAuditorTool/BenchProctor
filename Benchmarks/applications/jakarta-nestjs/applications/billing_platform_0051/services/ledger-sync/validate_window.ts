// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("ledger-sync")
export class ValidateWindow {
  @Post("validateWindow")
  async validateWindow(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body.payload as string) || "";
    const _raw = synopsis;
    const arrears = (_raw && _raw.length > 0) ? _raw : 'default';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(arrears));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const dunning = _parsed.data;
    childProcess.execSync("echo " + dunning);
    return { created: true };
  }
}
