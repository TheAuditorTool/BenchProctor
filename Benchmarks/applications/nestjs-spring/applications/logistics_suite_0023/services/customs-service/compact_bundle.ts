// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("customs-service")
export class CompactBundle {
  @Post("compactBundle")
  async compactBundle(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.payload as string) || "";
    const tokens = String(caption).split(',').filter((t) => t.length > 0);
    const parcel = tokens.join(' ');
    childProcess.execSync("echo " + parcel);
    return { created: true };
  }
}
