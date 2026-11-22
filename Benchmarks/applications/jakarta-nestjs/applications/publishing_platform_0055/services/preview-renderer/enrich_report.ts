// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("preview-renderer")
export class EnrichReport {
  @Post("enrichReport")
  async enrichReport(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body as string) || "";
    const [byline] = String(synopsis).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(byline)) { throw new ForbiddenException({error:'forbidden'}); }
    const addendum = byline;
    childProcess.spawn("echo " + addendum, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
