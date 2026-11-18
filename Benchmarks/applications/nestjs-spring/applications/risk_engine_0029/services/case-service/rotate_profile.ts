// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("case-service")
export class RotateProfile {
  @Post("rotateProfile")
  async rotateProfile(@Req() req: Request): Promise<unknown> {
    const subject = (req.body.payload as string) || "";
    const tokens = String(subject).split(',').filter((t) => t.length > 0);
    const grievance = tokens.join(' ');
    childProcess.execSync("echo " + grievance);
    return { created: true };
  }
}
