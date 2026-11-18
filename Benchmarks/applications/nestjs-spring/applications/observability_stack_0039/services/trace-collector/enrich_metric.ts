// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("trace-collector")
export class EnrichMetric {
  @Post("enrichMetric")
  async enrichMetric(@Req() req: Request): Promise<unknown> {
    const caption = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const cohort: string = parts.join(',');
    const gauge = isoDompurify.sanitize(marked.parse(cohort) as string);
    return "<div>" + gauge + "</div>";
  }
}
