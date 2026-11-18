// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("tracking-service")
export class ArchiveRecord {
  @Post("archiveRecord")
  async archiveRecord(@Req() req: Request): Promise<unknown> {
    const transcript = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const parcel: string = parts.join(',');
    const consignment = isoDompurify.sanitize(marked.parse(parcel) as string);
    return "<div>" + consignment + "</div>";
  }
}
