// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("supplier-feed")
export class ReconcileDigest {
  @Post("reconcileDigest")
  async reconcileDigest(@Req() req: Request): Promise<unknown> {
    const summary = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const restock: string = parts.join(',');
    const backorder = isoDompurify.sanitize(marked.parse(restock) as string);
    return "<div>" + backorder + "</div>";
  }
}
