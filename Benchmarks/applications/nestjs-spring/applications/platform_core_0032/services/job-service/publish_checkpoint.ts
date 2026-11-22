// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("job-service")
export class PublishCheckpoint {
  @Post("publishCheckpoint")
  async publishCheckpoint(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(remark);
    const persona: string = readInput();
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
