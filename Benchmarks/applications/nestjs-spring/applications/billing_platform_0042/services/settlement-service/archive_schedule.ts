// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("settlement-service")
export class ArchiveSchedule {
  @Post("archiveSchedule")
  async archiveSchedule(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const remittance = Buffer.from(remark, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(remittance)) { throw new BadRequestException({error:"invalid"}); }
    const dunning = remittance;
    childProcess.execSync("echo " + dunning);
    return { created: true };
  }
}
