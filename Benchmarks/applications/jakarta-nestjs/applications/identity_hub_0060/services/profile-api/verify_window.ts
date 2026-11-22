// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("profile-api")
export class VerifyWindow {
  @Post("verifyWindow")
  async verifyWindow(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body as string) || "";
    const [persona] = String(paragraph).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(persona)) { throw new ForbiddenException({error:'forbidden'}); }
    const blurb = persona;
    childProcess.spawn("echo " + blurb, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
