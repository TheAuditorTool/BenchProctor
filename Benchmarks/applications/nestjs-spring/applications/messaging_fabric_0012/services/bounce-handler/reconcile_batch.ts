// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("bounce-handler")
export class ReconcileBatch {
  @Post("reconcileBatch")
  async reconcileBatch(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["user-agent"] as string) || "";
    const bulletin = preface != null ? preface : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(bulletin));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const citation = _parsed.data;
    childProcess.exec("echo " + citation, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
