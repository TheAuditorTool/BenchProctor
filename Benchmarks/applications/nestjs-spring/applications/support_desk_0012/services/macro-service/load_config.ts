// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("macro-service")
export class LoadConfig {
  @Post("loadConfig")
  async loadConfig(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const tokens = String(summary).split(',').filter((t) => t.length > 0);
    const grievance = tokens.join(' ');
    childProcess.execSync("echo " + grievance);
    return { created: true };
  }
}
