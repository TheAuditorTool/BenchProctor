// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("alert-triage")
export class CompactRoster {
  @Post("compactRoster")
  async compactRoster(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    childProcess.execFileSync("echo", [grievance]);
    return { created: true };
  }
}
