// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("fx-service")
export class RenderWindow {
  @Post("renderWindow")
  async renderWindow(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.authorization as string) || "";
    const tokens = String(subject).split(',').filter((t) => t.length > 0);
    const ledger = tokens.join(' ');
    childProcess.execFileSync("echo", [ledger]);
    return { created: true };
  }
}
