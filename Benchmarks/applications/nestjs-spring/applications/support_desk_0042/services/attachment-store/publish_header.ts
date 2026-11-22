// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("attachment-store")
export class PublishHeader {
  @Post("publishHeader")
  async publishHeader(@Req() req: Request): Promise<unknown> {
    const blurb = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let inquiry;
    try { inquiry = JSON.parse(blurb).value || ""; }
    catch (e) { inquiry = String(blurb); }
    const grievance = isoDompurify.sanitize(marked.parse(inquiry) as string);
    return "<div>" + grievance + "</div>";
  }
}
