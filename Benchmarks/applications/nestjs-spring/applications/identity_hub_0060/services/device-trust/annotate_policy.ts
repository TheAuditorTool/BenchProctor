// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("device-trust")
export class AnnotatePolicy {
  @Post("annotatePolicy")
  async annotatePolicy(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body as string) || "";
    const _raw = paragraph;
    const persona = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(persona)) { throw new ForbiddenException({error:'forbidden'}); }
    const blurb = persona;
    childProcess.execSync("echo " + blurb);
    return { created: true };
  }
}
