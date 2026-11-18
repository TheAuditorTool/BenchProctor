// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("dispute-service")
export class ResolveIndex {
  @Post("resolveIndex")
  async resolveIndex(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers["user-agent"] as string) || "";
    const transform = (v: string): string => v.trim();
    const ledger: string = transform(subtitle);
    childProcess.execSync("echo " + ledger);
    return { created: true };
  }
}
