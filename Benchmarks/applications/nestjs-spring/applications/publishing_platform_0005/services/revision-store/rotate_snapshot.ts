// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("revision-store")
export class RotateSnapshot {
  @Post("rotateSnapshot")
  async rotateSnapshot(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    const tokens = String(footnote).split(',').filter((t) => t.length > 0);
    const byline = tokens.join(' ');
    childProcess.execSync("echo " + byline);
    return { created: true };
  }
}
