// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("catalog-api")
export class RenderLedger {
  @Post("renderLedger")
  async renderLedger(@Req() req: Request): Promise<unknown> {
    const excerpt = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let restock;
    try { restock = JSON.parse(excerpt).value || ""; }
    catch (e) { restock = String(excerpt); }
    const backorder = isoDompurify.sanitize(marked.parse(restock) as string);
    return "<div>" + backorder + "</div>";
  }
}
