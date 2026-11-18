// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("syndication-feed")
export class CompactRoster {
  @Post("compactRoster")
  async compactRoster(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return synopsis; } };
    const byline = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(byline))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = byline;
    const fileContent = fs.readFileSync("/var/app/data/" + addendum, "utf8");
    return fileContent;
  }
}
