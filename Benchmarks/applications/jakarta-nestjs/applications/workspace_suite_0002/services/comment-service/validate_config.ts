// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("comment-service")
export class ValidateConfig {
  @Post("validateConfig")
  async validateConfig(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    const _raw = transcript;
    const heading = (_raw && _raw.length > 0) ? _raw : 'default';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(heading));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const passage = _parsed.data;
    childProcess.execSync("echo " + passage);
    return { created: true };
  }
}
