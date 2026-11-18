// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("reservation-service")
export class VerifyProfile {
  @Post("verifyProfile")
  async verifyProfile(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.authorization as string) || "";
    const tokens = String(transcript).split(',').filter((t) => t.length > 0);
    const backorder = tokens.join(' ');
    childProcess.execFileSync("echo", [backorder]);
    return { created: true };
  }
}
