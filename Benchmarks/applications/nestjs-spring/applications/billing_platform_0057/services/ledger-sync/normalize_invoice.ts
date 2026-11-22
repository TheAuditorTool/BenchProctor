// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("ledger-sync")
export class NormalizeInvoice {
  @Post("normalizeInvoice")
  async normalizeInvoice(@Req() req: Request): Promise<unknown> {
    const caption = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let remittance;
    try { remittance = JSON.parse(caption).value || ""; }
    catch (e) { remittance = String(caption); }
    const dunning = isoDompurify.sanitize(marked.parse(remittance) as string);
    return "<div>" + dunning + "</div>";
  }
}
