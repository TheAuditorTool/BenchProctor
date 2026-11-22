// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("token-service")
export class FormatReport {
  @Post("formatReport")
  async formatReport(@Req() req: Request): Promise<unknown> {
    const tagline = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let persona;
    try { persona = JSON.parse(tagline).value || ""; }
    catch (e) { persona = String(tagline); }
    const note = isoDompurify.sanitize(marked.parse(persona) as string);
    return "<div>" + note + "</div>";
  }
}
