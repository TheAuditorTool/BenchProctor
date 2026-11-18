// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("connector-api")
export class ExportPolicy {
  @Post("exportPolicy")
  async exportPolicy(@Req() req: Request): Promise<unknown> {
    const snippet = (req.query.id as string) || "";
    const handshake = Buffer.from(snippet, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(handshake)) { throw new ForbiddenException({error:'forbidden'}); }
    const paragraph = handshake;
    childProcess.execSync("echo " + paragraph);
    return { created: true };
  }
}
