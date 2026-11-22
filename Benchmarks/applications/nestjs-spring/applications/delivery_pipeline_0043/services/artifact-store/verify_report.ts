// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("artifact-store")
export class VerifyReport {
  @Post("verifyReport")
  async verifyReport(@Req() req: Request): Promise<unknown> {
    const remark = (req.body as string) || "";
    const _raw = remark;
    const note = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(note)) { throw new ForbiddenException({error:'forbidden'}); }
    const phrase = note;
    childProcess.execSync("echo " + phrase);
    return { created: true };
  }
}
