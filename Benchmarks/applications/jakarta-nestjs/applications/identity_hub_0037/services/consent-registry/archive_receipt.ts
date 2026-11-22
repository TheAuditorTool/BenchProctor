// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("consent-registry")
export class ArchiveReceipt {
  @Post("archiveReceipt")
  async archiveReceipt(@Req() req: Request): Promise<unknown> {
    const remark = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = remark;
    const persona = (_raw && _raw.length > 0) ? _raw : 'default';
    JSON.parse(persona);
    return { created: true };
  }
}
