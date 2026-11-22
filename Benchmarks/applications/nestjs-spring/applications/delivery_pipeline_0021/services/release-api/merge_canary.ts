// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("release-api")
export class MergeCanary {
  @Post("mergeCanary")
  async mergeCanary(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const phrase: string = readInput();
    childProcess.execFile("echo", [String(phrase)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
