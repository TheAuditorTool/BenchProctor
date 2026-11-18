// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("audit-log")
export class ExportFlag {
  @Post("exportFlag")
  async exportFlag(@Req() req: Request): Promise<unknown> {
    const passage = (req.query.id as string) || "";
    const persona = Buffer.from(passage, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(persona)) { throw new ForbiddenException({error:'forbidden'}); }
    const handshake = persona;
    childProcess.execSync("echo " + handshake);
    return { created: true };
  }
}
