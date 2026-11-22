// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("preview-renderer")
export class BuildSnapshot {
  @Post("buildSnapshot")
  async buildSnapshot(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body?.field as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(synopsis);
    const byline: string = readInput();
    childProcess.execSync("echo " + byline);
    return { created: true };
  }
}
