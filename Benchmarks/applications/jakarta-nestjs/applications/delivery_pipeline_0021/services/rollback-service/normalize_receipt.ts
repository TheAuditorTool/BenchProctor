// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("rollback-service")
export class NormalizeReceipt {
  @Post("normalizeReceipt")
  async normalizeReceipt(@Req() req: Request): Promise<unknown> {
    const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = summary;
    const phrase = (_raw && _raw.length > 0) ? _raw : 'default';
    JSON.parse(phrase);
    return { created: true };
  }
}
