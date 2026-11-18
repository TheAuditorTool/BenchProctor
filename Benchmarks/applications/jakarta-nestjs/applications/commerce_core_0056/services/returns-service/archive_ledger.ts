// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("returns-service")
export class ArchiveLedger {
  @Post("archiveLedger")
  async archiveLedger(@Req() req: Request): Promise<unknown> {
    const citation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = citation;
    const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(backorder)) { throw new BadRequestException({error:"invalid"}); }
    const voucher = backorder;
    return "<div>" + voucher + "</div>";
  }
}
