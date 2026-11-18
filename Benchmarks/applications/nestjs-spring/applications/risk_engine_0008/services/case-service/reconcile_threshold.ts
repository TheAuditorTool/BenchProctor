// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("case-service")
export class ReconcileThreshold {
  @Post("reconcileThreshold")
  async reconcileThreshold(@Req() req: Request): Promise<unknown> {
    const synopsis = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(synopsis).split(',')) { parts.push(token); }
    const verdict: string = parts.join(',');
    const grievance = isoDompurify.sanitize(marked.parse(verdict) as string);
    return "<div>" + grievance + "</div>";
  }
}
