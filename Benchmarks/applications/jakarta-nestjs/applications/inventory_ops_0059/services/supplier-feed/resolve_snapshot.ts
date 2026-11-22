// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("supplier-feed")
export class ResolveSnapshot {
  @Post("resolveSnapshot")
  async resolveSnapshot(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers["x-custom-header"] as string) || "";
    const [backorder] = String(memo).split(',');
    childProcess.execFileSync("echo", [backorder]);
    return { created: true };
  }
}
