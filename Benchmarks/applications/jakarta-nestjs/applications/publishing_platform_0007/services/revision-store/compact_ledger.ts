// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("revision-store")
export class CompactLedger {
  @Post("compactLedger")
  async compactLedger(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.referer as string) || "";
    const _raw = remark;
    const byline = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(byline))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = byline;
    childProcess.exec("echo " + addendum, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
