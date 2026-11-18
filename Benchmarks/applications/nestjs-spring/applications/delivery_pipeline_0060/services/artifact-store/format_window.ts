// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("artifact-store")
export class FormatWindow {
  @Post("formatWindow")
  async formatWindow(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.authorization as string) || "";
    const tokens = String(wording).split(',').filter((t) => t.length > 0);
    const remark = tokens.join(' ');
    childProcess.execFileSync("echo", [remark]);
    return { created: true };
  }
}
