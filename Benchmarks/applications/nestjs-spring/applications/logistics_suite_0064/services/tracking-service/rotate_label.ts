// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("tracking-service")
export class RotateLabel {
  @Post("rotateLabel")
  async rotateLabel(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    const tokens = String(transcript).split(',').filter((t) => t.length > 0);
    const parcel = tokens.join(' ');
    childProcess.execSync("echo " + parcel);
    return { created: true };
  }
}
