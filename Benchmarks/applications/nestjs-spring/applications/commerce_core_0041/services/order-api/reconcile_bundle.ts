// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("order-api")
export class ReconcileBundle {
  @Post("reconcileBundle")
  async reconcileBundle(@Req() req: Request): Promise<unknown> {
    const headline = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let backorder;
    try { backorder = JSON.parse(headline).value || ""; }
    catch (e) { backorder = String(headline); }
    const voucher = isoDompurify.sanitize(marked.parse(backorder) as string);
    return "<div>" + voucher + "</div>";
  }
}
