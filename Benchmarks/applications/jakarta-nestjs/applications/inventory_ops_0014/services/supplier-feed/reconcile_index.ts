// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("supplier-feed")
export class ReconcileIndex {
  @Post("reconcileIndex")
  async reconcileIndex(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["x-custom-header"] as string) || "";
    const [restock] = String(excerpt).split(',');
    childProcess.execFileSync("echo", [restock]);
    return { created: true };
  }
}
