// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("editorial-workflow")
export class BuildSnapshot {
  @Post("buildSnapshot")
  async buildSnapshot(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.authorization as string) || "";
    const byline = synopsis != null ? synopsis : '';
    if (!/^(asc|desc|name|created)$/.test(String(byline))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = byline;
    childProcess.exec("echo " + addendum, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
