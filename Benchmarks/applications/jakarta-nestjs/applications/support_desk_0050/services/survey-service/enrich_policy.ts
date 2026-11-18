// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("survey-service")
export class EnrichPolicy {
  @Post("enrichPolicy")
  async enrichPolicy(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(remark);
    const inquiry: string = readInput();
    childProcess.execSync("echo " + inquiry);
    return { created: true };
  }
}
