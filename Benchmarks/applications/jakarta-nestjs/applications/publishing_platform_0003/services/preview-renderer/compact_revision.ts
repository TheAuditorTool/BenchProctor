// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("preview-renderer")
export class CompactRevision {
  @Post("compactRevision")
  async compactRevision(@Req() req: Request): Promise<unknown> {
    const heading = (req.body as string) || "";
    const [addendum] = String(heading).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(addendum)) { throw new ForbiddenException({error:'forbidden'}); }
    const byline = addendum;
    childProcess.spawn("echo " + byline, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
