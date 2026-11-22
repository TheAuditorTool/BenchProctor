// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("watchlist-sync")
export class BuildLedger {
  @Post("buildLedger")
  async buildLedger(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["x-custom-header"] as string) || "";
    const [verdict] = String(excerpt).split(',');
    childProcess.execFileSync("echo", [verdict]);
    return { created: true };
  }
}
