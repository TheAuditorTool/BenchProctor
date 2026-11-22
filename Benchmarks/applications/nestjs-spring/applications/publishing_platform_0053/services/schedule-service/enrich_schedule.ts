// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("schedule-service")
export class EnrichSchedule {
  @Post("enrichSchedule")
  async enrichSchedule(@Req() req: Request): Promise<unknown> {
    const note = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let byline;
    try { byline = JSON.parse(note).value || ""; }
    catch (e) { byline = String(note); }
    const addendum = isoDompurify.sanitize(marked.parse(byline) as string);
    return "<div>" + addendum + "</div>";
  }
}
