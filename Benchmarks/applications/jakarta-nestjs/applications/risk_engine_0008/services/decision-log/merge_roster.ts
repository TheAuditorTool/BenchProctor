// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("decision-log")
export class MergeRoster {
  @Post("mergeRoster")
  async mergeRoster(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(synopsis).split(',')) { parts.push(token); }
    const verdict: string = parts.join(',');
    childProcess.execFileSync("echo", [verdict]);
    return { created: true };
  }
}
