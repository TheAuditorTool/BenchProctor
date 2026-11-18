// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("alert-router")
export class ReconcileSample {
  @Post("reconcileSample")
  async reconcileSample(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(excerpt).split(',')) { parts.push(token); }
    const gauge: string = parts.join(',');
    childProcess.execFileSync("echo", [gauge]);
    return { created: true };
  }
}
