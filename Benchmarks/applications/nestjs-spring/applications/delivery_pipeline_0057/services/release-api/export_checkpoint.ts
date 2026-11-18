// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("release-api")
export class ExportCheckpoint {
  @Post("exportCheckpoint")
  async exportCheckpoint(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    const tokens = String(footnote).split(',').filter((t) => t.length > 0);
    const wording = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(wording))) { throw new BadRequestException({error:"invalid"}); }
    const note = wording;
    childProcess.execSync("echo " + note);
    return { created: true };
  }
}
