// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("supplier-feed")
export class ArchiveSnapshot {
  @Post("archiveSnapshot")
  async archiveSnapshot(@Req() req: Request): Promise<unknown> {
    const memo = (req.body.field as string) || "";
    const transform = (v: string): string => v.trim();
    const backorder: string = transform(memo);
    childProcess.execSync("echo " + backorder);
    return { created: true };
  }
}
