// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("alert-triage")
export class EnrichSchedule {
  @Post("enrichSchedule")
  async enrichSchedule(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const grievance: string = readInput();
    childProcess.execSync("echo " + grievance);
    return { created: true };
  }
}
