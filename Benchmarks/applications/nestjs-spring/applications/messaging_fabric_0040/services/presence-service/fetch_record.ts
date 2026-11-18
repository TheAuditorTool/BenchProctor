// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("presence-service")
export class FetchRecord {
  @Post("fetchRecord")
  async fetchRecord(@Req() req: Request): Promise<unknown> {
    const preface = (req.query.id as string) || "";
    const bulletin = Buffer.from(preface, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(bulletin)) { throw new BadRequestException({error:"invalid"}); }
    const notice = bulletin;
    childProcess.execSync("echo " + notice);
    return { created: true };
  }
}
