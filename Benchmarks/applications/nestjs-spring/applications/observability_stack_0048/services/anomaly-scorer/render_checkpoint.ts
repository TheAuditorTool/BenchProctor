// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("anomaly-scorer")
export class RenderCheckpoint {
  @Post("renderCheckpoint")
  async renderCheckpoint(@Req() req: Request): Promise<unknown> {
    const excerpt = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(excerpt).split(',')) { parts.push(token); }
    const gauge: string = parts.join(',');
    return "<div>" + gauge + "</div>";
  }
}
