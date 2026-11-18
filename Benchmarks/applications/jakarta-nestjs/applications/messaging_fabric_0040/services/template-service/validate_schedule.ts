// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("template-service")
export class ValidateSchedule {
  @Post("validateSchedule")
  async validateSchedule(@Req() req: Request): Promise<unknown> {
    const preface = (req.body.payload as string) || "";
    const _raw = preface;
    const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(bulletin));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const notice = _parsed.data;
    childProcess.execSync("echo " + notice);
    return { created: true };
  }
}
