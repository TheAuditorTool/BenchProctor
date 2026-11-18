// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("audit-log")
export class CollectDigest {
  @Post("collectDigest")
  async collectDigest(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers["user-agent"] as string) || "";
    const tokens = String(tagline).split(',').filter((t) => t.length > 0);
    const persona = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    childProcess.execSync("echo " + handshake);
    return { created: true };
  }
}
