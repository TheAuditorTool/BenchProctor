// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("activity-feed")
export class AnnotateSnapshot {
  @Post("annotateSnapshot")
  async annotateSnapshot(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers.referer as string) || "";
    const _raw = paragraph;
    const wording = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(wording))) { throw new BadRequestException({error:"invalid"}); }
    const transcript = wording;
    childProcess.exec("echo " + transcript, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
