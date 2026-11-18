// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("artifact-store")
export class ArchiveBatch {
  @Post("archiveBatch")
  async archiveBatch(@Req() req: Request): Promise<unknown> {
    const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const remark: string = parts.join(',');
    return "<div>" + remark + "</div>";
  }
}
