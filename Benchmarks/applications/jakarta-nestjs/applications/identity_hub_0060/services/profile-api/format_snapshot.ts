// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("profile-api")
export class FormatSnapshot {
  @Post("formatSnapshot")
  async formatSnapshot(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body?.field as string) || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(paragraph);
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
