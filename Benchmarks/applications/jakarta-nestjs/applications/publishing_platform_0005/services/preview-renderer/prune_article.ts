// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("preview-renderer")
export class PruneArticle {
  @Post("pruneArticle")
  async pruneArticle(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.field as string) || "";
    const _input = String(footnote);
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
