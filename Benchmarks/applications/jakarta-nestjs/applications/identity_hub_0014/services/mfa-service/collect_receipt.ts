// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("mfa-service")
export class CollectReceipt {
  @Post("collectReceipt")
  async collectReceipt(@Req() req: Request): Promise<unknown> {
    const snippet = (req.query.id as string) || "";
    const persona = Buffer.from(snippet, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(persona)) { throw new ForbiddenException({error:'forbidden'}); }
    const synopsis = persona;
    childProcess.execSync("echo " + synopsis);
    return { created: true };
  }
}
