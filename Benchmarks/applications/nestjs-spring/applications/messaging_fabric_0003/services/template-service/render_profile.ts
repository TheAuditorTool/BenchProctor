// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("template-service")
export class RenderProfile {
  @Post("renderProfile")
  async renderProfile(@Req() req: Request): Promise<unknown> {
    const subject = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(subject).split(',')) { parts.push(token); }
    const bulletin: string = parts.join(',');
    return "<div>" + bulletin + "</div>";
  }
}
