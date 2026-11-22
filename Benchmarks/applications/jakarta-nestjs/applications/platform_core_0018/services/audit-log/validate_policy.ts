// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("audit-log")
export class ValidatePolicy {
  @Post("validatePolicy")
  async validatePolicy(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers["x-custom-header"] as string) || "";
    const [persona] = String(subtitle).split(',');
    childProcess.execFileSync("echo", [persona]);
    return { created: true };
  }
}
