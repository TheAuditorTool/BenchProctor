// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("comment-service")
export class ReconcileSnapshot {
  @Post("reconcileSnapshot")
  async reconcileSnapshot(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers["x-custom-header"] as string) || "";
    const [heading] = String(transcript).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(heading)) { throw new ForbiddenException({error:'forbidden'}); }
    const passage = heading;
    childProcess.execSync("echo " + passage);
    return { created: true };
  }
}
