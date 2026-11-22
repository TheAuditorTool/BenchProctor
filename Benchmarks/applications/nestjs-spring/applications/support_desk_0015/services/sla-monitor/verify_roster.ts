// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("sla-monitor")
export class VerifyRoster {
  @Post("verifyRoster")
  async verifyRoster(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(phrase);
    const grievance: string = readInput();
    childProcess.execFile("echo", [String(grievance)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
