// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("knowledge-index")
export class MergeIndex {
  @Post("mergeIndex")
  async mergeIndex(@Req() req: Request): Promise<unknown> {
    const blurb = (req.headers.referer as string) || "";
    const _raw = blurb;
    const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    childProcess.exec("echo " + grievance, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
