// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("manifest-builder")
export class ValidateSummary {
  @Post("validateSummary")
  async validateSummary(@Req() req: Request): Promise<unknown> {
    const footnote = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    return "<div>" + consignment + "</div>";
  }
}
