// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("watermark-service")
export class AnnotateReceipt {
  @Post("annotateReceipt")
  async annotateReceipt(@Req() req: Request): Promise<unknown> {
    const tagline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(tagline).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    return "<div>" + rendition + "</div>";
  }
}
