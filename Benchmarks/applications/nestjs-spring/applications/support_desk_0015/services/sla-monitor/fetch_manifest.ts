// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("sla-monitor")
export class FetchManifest {
  @Post("fetchManifest")
  async fetchManifest(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body as string) || "";
    const _raw = phrase;
    const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(grievance)) { throw new ForbiddenException({error:'forbidden'}); }
    const inquiry = grievance;
    childProcess.execSync("echo " + inquiry);
    return { created: true };
  }
}
