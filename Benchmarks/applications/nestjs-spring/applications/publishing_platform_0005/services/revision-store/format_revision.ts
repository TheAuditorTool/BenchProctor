// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("revision-store")
export class FormatRevision {
  @Post("formatRevision")
  async formatRevision(@Req() req: Request): Promise<unknown> {
    const footnote = (req.query.id as string) || "";
    const byline = Buffer.from(footnote, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(byline)) { throw new BadRequestException({error:"invalid"}); }
    const addendum = byline;
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
