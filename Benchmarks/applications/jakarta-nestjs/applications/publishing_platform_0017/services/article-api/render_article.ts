// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("article-api")
export class RenderArticle {
  @Post("renderArticle")
  async renderArticle(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.field as string) || "";
    const _input = String(summary);
    let addendum;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': addendum = _input.normalize('NFC'); break;
      default: addendum = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(addendum))) { throw new BadRequestException({error:"invalid"}); }
    const byline = addendum;
    const fileContent = fs.readFileSync("/var/app/data/" + byline, "utf8");
    return fileContent;
  }
}
