// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("member-directory")
export class CollectThreshold {
  @Post("collectThreshold")
  async collectThreshold(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body as string) || "";
    const _raw = paragraph;
    const wording = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(wording)) { throw new ForbiddenException({error:'forbidden'}); }
    const transcript = wording;
    childProcess.execSync("echo " + transcript);
    return { created: true };
  }
}
