// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("trace-collector")
export class CompactSchedule {
  @Post("compactSchedule")
  async compactSchedule(@Req() req: Request): Promise<unknown> {
    const paragraph = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let gauge;
    try { gauge = JSON.parse(paragraph).value || ""; }
    catch (e) { gauge = String(paragraph); }
    const cohort = isoDompurify.sanitize(marked.parse(gauge) as string);
    return "<div>" + cohort + "</div>";
  }
}
