// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("trace-collector")
export class PruneDigest {
  @Post("pruneDigest")
  async pruneDigest(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(paragraph);
    const gauge: string = readInput();
    childProcess.execSync("echo " + gauge);
    return { created: true };
  }
}
