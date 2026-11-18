// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("changelog-builder")
export class PruneIndex {
  @Post("pruneIndex")
  async pruneIndex(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.field as string) || "";
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const wording: string = parts.join(',');
    childProcess.execSync("echo " + wording);
    return { created: true };
  }
}
