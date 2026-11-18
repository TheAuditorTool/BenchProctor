// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("template-service")
export class LoadRecord {
  @Post("loadRecord")
  async loadRecord(@Req() req: Request): Promise<unknown> {
    const subject = (req.query.id as string) || "";
    const bulletin = Buffer.from(subject, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(bulletin)) { throw new BadRequestException({error:"invalid"}); }
    const passage = bulletin;
    childProcess.execSync("echo " + passage);
    return { created: true };
  }
}
