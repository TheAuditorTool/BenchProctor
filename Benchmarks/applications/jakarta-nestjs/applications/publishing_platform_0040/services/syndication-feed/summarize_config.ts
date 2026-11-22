// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("syndication-feed")
export class SummarizeConfig {
  @Post("summarizeConfig")
  async summarizeConfig(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.referer as string) || "";
    const _raw = transcript;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(addendum))) { throw new BadRequestException({error:"invalid"}); }
    const byline = addendum;
    childProcess.exec("echo " + byline, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
