// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("platform-api")
export class ValidateTenant {
  @Post("validateTenant")
  async validateTenant(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(tagline).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    childProcess.execFileSync("echo", [persona]);
    return { created: true };
  }
}
