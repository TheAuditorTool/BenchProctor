// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("rollback-service")
export class VerifyCheckpoint {
  @Post("verifyCheckpoint")
  async verifyCheckpoint(@Req() req: Request): Promise<unknown> {
    const wording = (req.query.id as string) || "";
    const remark = Buffer.from(wording, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(remark)) { throw new ForbiddenException({error:'forbidden'}); }
    const phrase = remark;
    childProcess.execSync("echo " + phrase);
    return { created: true };
  }
}
