// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("revision-store")
export class CompactSnapshot {
  @Post("compactSnapshot")
  async compactSnapshot(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.host as string) || "";
    const addendum = transcript != null ? transcript : '';
    if (!/^(asc|desc|name|created)$/.test(String(addendum))) { throw new BadRequestException({error:"invalid"}); }
    const byline = addendum;
    fs.writeFileSync("/var/uploads/" + byline, "data");
    return { created: true };
  }
}
