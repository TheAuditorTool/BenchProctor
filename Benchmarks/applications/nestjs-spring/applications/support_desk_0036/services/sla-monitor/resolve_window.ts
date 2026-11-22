// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("sla-monitor")
export class ResolveWindow {
  @Post("resolveWindow")
  async resolveWindow(@Req() req: Request): Promise<unknown> {
    const preface = (req.body.payload as string) || "";
    let grievance;
    try { grievance = JSON.parse(preface).value || ""; }
    catch (e) { grievance = String(preface); }
    childProcess.exec("echo " + grievance, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
