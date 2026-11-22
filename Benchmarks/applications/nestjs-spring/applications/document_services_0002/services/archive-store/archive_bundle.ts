// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("archive-store")
export class ArchiveBundle {
  @Post("archiveBundle")
  async archiveBundle(@Req() req: Request): Promise<unknown> {
    const wording = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let addendum;
    try { addendum = JSON.parse(wording).value || ""; }
    catch (e) { addendum = String(wording); }
    const dossier = isoDompurify.sanitize(marked.parse(addendum) as string);
    return "<div>" + dossier + "</div>";
  }
}
