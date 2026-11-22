// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("release-api")
export class MergeWindow {
  @Post("mergeWindow")
  async mergeWindow(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.host as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const phrase: string = parts.join(',');
    fs.writeFileSync("/var/uploads/" + phrase, "data");
    return { created: true };
  }
}
