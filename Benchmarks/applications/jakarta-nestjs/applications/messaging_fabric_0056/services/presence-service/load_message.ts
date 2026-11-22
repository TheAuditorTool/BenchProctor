// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("presence-service")
export class LoadMessage {
  @Post("loadMessage")
  async loadMessage(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.referer as string) || "";
    const _raw = footnote;
    const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const snippet = bulletin;
    childProcess.exec("echo " + snippet, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
