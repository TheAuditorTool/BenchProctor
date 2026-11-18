// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("retention-service")
export class ExportSummary {
  @Post("exportSummary")
  async exportSummary(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const cohort: string = parts.join(',');
    childProcess.execFileSync("echo", [cohort]);
    return { created: true };
  }
}
