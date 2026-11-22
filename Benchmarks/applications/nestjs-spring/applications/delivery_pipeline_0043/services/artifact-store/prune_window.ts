// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("artifact-store")
export class PruneWindow {
  @Post("pruneWindow")
  async pruneWindow(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const note = remark != null ? remark : '';
    if (!/^(asc|desc|name|created)$/.test(String(note))) { throw new BadRequestException({error:"invalid"}); }
    const phrase = note;
    childProcess.exec("echo " + phrase, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
