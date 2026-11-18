// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("config-service")
export class PruneDigest {
  @Post("pruneDigest")
  async pruneDigest(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(notice);
    const persona: string = readInput();
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
