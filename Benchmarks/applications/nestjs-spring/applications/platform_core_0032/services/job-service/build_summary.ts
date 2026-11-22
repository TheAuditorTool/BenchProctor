// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("job-service")
export class BuildSummary {
  @Post("buildSummary")
  async buildSummary(@Req() req: Request): Promise<unknown> {
    const remark = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let persona;
    try { persona = JSON.parse(remark).value || ""; }
    catch (e) { persona = String(remark); }
    const handshake = isoDompurify.sanitize(marked.parse(persona) as string);
    return "<div>" + handshake + "</div>";
  }
}
