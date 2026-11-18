// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("secret-broker")
export class BuildReceipt {
  @Post("buildReceipt")
  async buildReceipt(@Req() req: Request): Promise<unknown> {
    const snippet = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(snippet).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    return "<div>" + persona + "</div>";
  }
}
