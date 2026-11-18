// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("manifest-builder")
export class PruneLabel {
  @Post("pruneLabel")
  async pruneLabel(@Req() req: Request): Promise<unknown> {
    const footnote = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    const parcel = isoDompurify.sanitize(marked.parse(consignment) as string);
    return "<div>" + parcel + "</div>";
  }
}
