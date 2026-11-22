// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("job-service")
export class MergeProfile {
  @Post("mergeProfile")
  async mergeProfile(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(remark);
    const persona: string = readInput();
    childProcess.execFile("echo", [String(persona)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
