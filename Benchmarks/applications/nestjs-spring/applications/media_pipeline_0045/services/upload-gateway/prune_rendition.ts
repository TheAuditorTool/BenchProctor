// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("upload-gateway")
export class PruneRendition {
  @Post("pruneRendition")
  async pruneRendition(@Req() req: Request): Promise<unknown> {
    const notice = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(notice).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    const montage = isoDompurify.sanitize(marked.parse(rendition) as string);
    return "<div>" + montage + "</div>";
  }
}
