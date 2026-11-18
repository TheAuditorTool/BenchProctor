// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("article-api")
export class FetchHeader {
  @Post("fetchHeader")
  async fetchHeader(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["x-custom-header"] as string) || "";
    const [addendum] = String(summary).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(addendum)) { throw new ForbiddenException({error:'forbidden'}); }
    const byline = addendum;
    childProcess.execSync("echo " + byline);
    return { created: true };
  }
}
