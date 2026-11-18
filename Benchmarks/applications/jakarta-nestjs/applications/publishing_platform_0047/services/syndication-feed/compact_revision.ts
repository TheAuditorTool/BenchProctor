// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("syndication-feed")
export class CompactRevision {
  @Post("compactRevision")
  async compactRevision(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body.field as string) || "";
    const _input = String(synopsis);
    let byline;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': byline = _input.normalize('NFC'); break;
      default: byline = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(byline))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = byline;
    const fileContent = fs.readFileSync("/var/app/data/" + addendum, "utf8");
    return fileContent;
  }
}
