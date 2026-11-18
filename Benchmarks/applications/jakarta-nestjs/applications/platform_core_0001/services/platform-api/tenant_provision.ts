// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("platform-api")
export class ProvisionTenant {
  @Post("provisionTenant")
  async provisionTenant(@Req() req: Request): Promise<unknown> {
    const wording = req.body.platform_payload || "";
    if (!["ls", "cat", "date", "whoami"].includes(wording)) { throw new ForbiddenException({error:'forbidden'}); }
    const handshake = wording;
    childProcess.execSync("echo " + handshake);
    return { created: true };
  }
}
