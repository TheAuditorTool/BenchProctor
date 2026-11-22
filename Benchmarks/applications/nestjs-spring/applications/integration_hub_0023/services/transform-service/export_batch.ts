// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("transform-service")
export class ExportBatch {
  @Post("exportBatch")
  async exportBatch(@Req() req: Request): Promise<unknown> {
    const caption = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let handshake;
    try { handshake = JSON.parse(caption).value || ""; }
    catch (e) { handshake = String(caption); }
    const subject = isoDompurify.sanitize(marked.parse(handshake) as string);
    return "<div>" + subject + "</div>";
  }
}
