// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("presence-service")
export class LoadRecord {
  @Post("loadRecord")
  async loadRecord(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    const [bulletin] = String(footnote).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(bulletin)) { throw new ForbiddenException({error:'forbidden'}); }
    const snippet = bulletin;
    childProcess.spawn("echo " + snippet, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
