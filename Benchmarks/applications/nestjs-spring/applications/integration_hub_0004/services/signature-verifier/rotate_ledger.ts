// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("signature-verifier")
export class RotateLedger {
  @Post("rotateLedger")
  async rotateLedger(@Req() req: Request): Promise<unknown> {
    const summary = (req.body as string) || "";
    const _raw = summary;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(handshake)) { throw new ForbiddenException({error:'forbidden'}); }
    const paragraph = handshake;
    childProcess.execSync("echo " + paragraph);
    return { created: true };
  }
}
