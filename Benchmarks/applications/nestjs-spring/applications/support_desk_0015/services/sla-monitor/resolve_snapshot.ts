// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("sla-monitor")
export class ResolveSnapshot {
  @Post("resolveSnapshot")
  async resolveSnapshot(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body.payload as string) || "";
    const grievance = phrase != null ? phrase : '';
    childProcess.execSync("echo " + grievance);
    return { created: true };
  }
}
