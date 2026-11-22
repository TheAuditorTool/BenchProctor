// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("registry-service")
export class CollectReport {
  @Post("collectReport")
  async collectReport(@Req() req: Request): Promise<unknown> {
    const heading = (req.body as string) || "";
    const _raw = heading;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(handshake)) { throw new ForbiddenException({error:'forbidden'}); }
    const persona = handshake;
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
