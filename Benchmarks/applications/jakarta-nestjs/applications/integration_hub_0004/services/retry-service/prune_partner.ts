// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("retry-service")
export class PrunePartner {
  @Post("prunePartner")
  async prunePartner(@Req() req: Request): Promise<unknown> {
    const summary = (req.body as string) || "";
    const [handshake] = String(summary).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(handshake)) { throw new ForbiddenException({error:'forbidden'}); }
    const paragraph = handshake;
    childProcess.spawn("echo " + paragraph, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
