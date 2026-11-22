// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("rollback-service")
export class MergeHeader {
  @Post("mergeHeader")
  async mergeHeader(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const _raw = summary;
    const phrase = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(phrase))) { throw new BadRequestException({error:"invalid"}); }
    const subtitle = phrase;
    childProcess.exec("echo " + subtitle, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
