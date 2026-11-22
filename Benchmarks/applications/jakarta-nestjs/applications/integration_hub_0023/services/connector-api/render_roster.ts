// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("connector-api")
export class RenderRoster {
  @Post("renderRoster")
  async renderRoster(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.referer as string) || "";
    const _raw = caption;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const subject = handshake;
    childProcess.exec("echo " + subject, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
