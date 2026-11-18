// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("recovery-service")
export class ExportHeader {
  @Post("exportHeader")
  async exportHeader(@Req() req: Request): Promise<unknown> {
    const paragraph = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(paragraph).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    const synopsis = isoDompurify.sanitize(marked.parse(persona) as string);
    return "<div>" + synopsis + "</div>";
  }
}
