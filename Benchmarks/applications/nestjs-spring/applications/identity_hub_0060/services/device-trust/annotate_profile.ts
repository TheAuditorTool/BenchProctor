// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("device-trust")
export class AnnotateProfile {
  @Post("annotateProfile")
  async annotateProfile(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(paragraph);
    const persona: string = readInput();
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
