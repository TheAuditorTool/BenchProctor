// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("partner-registry")
export class RenderSnapshot {
  @Post("renderSnapshot")
  async renderSnapshot(@Req() req: Request): Promise<unknown> {
    const blurb = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(blurb).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    const citation = isoDompurify.sanitize(marked.parse(handshake) as string);
    return "<div>" + citation + "</div>";
  }
}
