// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("digest-service")
export class CompactChannel {
  @Post("compactChannel")
  async compactChannel(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(footnote);
    const bulletin: string = readInput();
    childProcess.execSync("echo " + bulletin);
    return { created: true };
  }
}
