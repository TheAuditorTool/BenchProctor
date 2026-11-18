// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("mapping-store")
export class FormatPolicy {
  @Post("formatPolicy")
  async formatPolicy(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    const tokens = String(footnote).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const blurb = handshake;
    childProcess.execSync("echo " + blurb);
    return { created: true };
  }
}
