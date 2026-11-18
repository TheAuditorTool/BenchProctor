// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("artifact-store")
export class PublishHeader {
  @Post("publishHeader")
  async publishHeader(@Req() req: Request): Promise<unknown> {
    const wording = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const remark: string = parts.join(',');
    const phrase = isoDompurify.sanitize(marked.parse(remark) as string);
    return "<div>" + phrase + "</div>";
  }
}
