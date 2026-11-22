// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("address-validator")
export class PublishRecord {
  @Post("publishRecord")
  async publishRecord(@Req() req: Request): Promise<unknown> {
    const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = summary;
    const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
    JSON.parse(consignment);
    return { created: true };
  }
}
