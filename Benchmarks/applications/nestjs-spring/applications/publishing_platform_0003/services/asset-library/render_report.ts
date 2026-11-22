// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("asset-library")
export class RenderReport {
  @Post("renderReport")
  async renderReport(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.authorization as string) || "";
    const addendum = heading != null ? heading : '';
    if (!/^(asc|desc|name|created)$/.test(String(addendum))) { throw new BadRequestException({error:"invalid"}); }
    const byline = addendum;
    childProcess.exec("echo " + byline, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
