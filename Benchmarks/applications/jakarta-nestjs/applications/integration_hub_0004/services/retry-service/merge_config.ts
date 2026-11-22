// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("retry-service")
export class MergeConfig {
  @Post("mergeConfig")
  async mergeConfig(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.referer as string) || "";
    const _raw = summary;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const paragraph = handshake;
    childProcess.exec("echo " + paragraph, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
