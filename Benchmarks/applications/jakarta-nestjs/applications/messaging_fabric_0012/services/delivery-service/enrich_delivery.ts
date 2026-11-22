// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("delivery-service")
export class EnrichDelivery {
  @Post("enrichDelivery")
  async enrichDelivery(@Req() req: Request): Promise<unknown> {
    const preface = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = preface;
    const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
    JSON.parse(bulletin);
    return { created: true };
  }
}
