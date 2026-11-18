// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("upload-gateway")
export class BuildHeader {
  @Post("buildHeader")
  async buildHeader(@Req() req: Request): Promise<unknown> {
    const notice = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(notice).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    return "<div>" + rendition + "</div>";
  }
}
