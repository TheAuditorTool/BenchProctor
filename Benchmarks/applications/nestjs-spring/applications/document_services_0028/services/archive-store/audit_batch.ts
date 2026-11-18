// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("archive-store")
export class AuditBatch {
  @Post("auditBatch")
  async auditBatch(@Req() req: Request): Promise<unknown> {
    const note = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(note).split(',')) { parts.push(token); }
    const addendum: string = parts.join(',');
    const dossier = isoDompurify.sanitize(marked.parse(addendum) as string);
    return "<div>" + dossier + "</div>";
  }
}
