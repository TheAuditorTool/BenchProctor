// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("artifact-store")
export class PruneHeader {
  @Post("pruneHeader")
  async pruneHeader(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers["user-agent"] as string) || "";
    const tokens = String(wording).split(',').filter((t) => t.length > 0);
    const remark = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(remark))) { throw new BadRequestException({error:"invalid"}); }
    const phrase = remark;
    childProcess.execSync("echo " + phrase);
    return { created: true };
  }
}
