// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("returns-service")
export class CollectLedger {
  @Post("collectLedger")
  async collectLedger(@Req() req: Request): Promise<unknown> {
    const citation = (req.query.id as string) || "";
    const backorder = Buffer.from(citation, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(backorder)) { throw new ForbiddenException({error:'forbidden'}); }
    const voucher = backorder;
    childProcess.execSync("echo " + voucher);
    return { created: true };
  }
}
