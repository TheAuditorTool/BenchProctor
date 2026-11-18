// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("asset-library")
export class ArchiveSchedule {
  @Post("archiveSchedule")
  async archiveSchedule(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers["user-agent"] as string) || "";
    const tokens = String(synopsis).split(',').filter((t) => t.length > 0);
    const byline = tokens.join(' ');
    childProcess.execSync("echo " + byline);
    return { created: true };
  }
}
