// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("allocation-service")
export class SummarizeAllocation {
  @Post("summarizeAllocation")
  async summarizeAllocation(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.field as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const restock: string = parts.join(',');
    childProcess.execSync("echo " + restock);
    return { created: true };
  }
}
