// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("macro-service")
export class RenderThreshold {
  @Post("renderThreshold")
  async renderThreshold(@Req() req: Request): Promise<unknown> {
    const phrase = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(phrase).split(',')) { parts.push(token); }
    const inquiry: string = parts.join(',');
    const grievance = isoDompurify.sanitize(marked.parse(inquiry) as string);
    return "<div>" + grievance + "</div>";
  }
}
