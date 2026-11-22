// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("payment-gateway")
export class RotateSnapshot {
  @Post("rotateSnapshot")
  async rotateSnapshot(@Req() req: Request): Promise<unknown> {
    const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = caption;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    JSON.parse(remittance);
    return { created: true };
  }
}
