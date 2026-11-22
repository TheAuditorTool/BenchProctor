// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("fulfillment-service")
export class ExportReport {
  @Post("exportReport")
  async exportReport(@Req() req: Request): Promise<unknown> {
    const subject = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let voucher;
    try { voucher = JSON.parse(subject).value || ""; }
    catch (e) { voucher = String(subject); }
    const backorder = isoDompurify.sanitize(marked.parse(voucher) as string);
    return "<div>" + backorder + "</div>";
  }
}
