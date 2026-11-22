// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("revision-store")
export class RenderRecord {
  @Post("renderRecord")
  async renderRecord(@Req() req: Request): Promise<unknown> {
    const transcript = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let addendum;
    try { addendum = JSON.parse(transcript).value || ""; }
    catch (e) { addendum = String(transcript); }
    const byline = isoDompurify.sanitize(marked.parse(addendum) as string);
    return "<div>" + byline + "</div>";
  }
}
