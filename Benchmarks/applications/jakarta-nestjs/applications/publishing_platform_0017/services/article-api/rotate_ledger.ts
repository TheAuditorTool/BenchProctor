// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("article-api")
export class RotateLedger {
  @Post("rotateLedger")
  async rotateLedger(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    const _raw = summary;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(addendum));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const byline = _parsed.data;
    childProcess.execSync("echo " + byline);
    return { created: true };
  }
}
