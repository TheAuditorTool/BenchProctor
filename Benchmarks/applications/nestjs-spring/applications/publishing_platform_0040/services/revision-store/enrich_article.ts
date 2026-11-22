// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("revision-store")
export class EnrichArticle {
  @Post("enrichArticle")
  async enrichArticle(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body as string) || "";
    const _raw = transcript;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(addendum)) { throw new ForbiddenException({error:'forbidden'}); }
    const byline = addendum;
    childProcess.execSync("echo " + byline);
    return { created: true };
  }
}
