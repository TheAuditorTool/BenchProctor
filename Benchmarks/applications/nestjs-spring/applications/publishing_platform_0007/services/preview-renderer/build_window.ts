// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("preview-renderer")
export class BuildWindow {
  @Post("buildWindow")
  async buildWindow(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const byline: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(byline))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = byline;
    fs.unlinkSync("/var/app/data/" + addendum);
    return { created: true };
  }
}
