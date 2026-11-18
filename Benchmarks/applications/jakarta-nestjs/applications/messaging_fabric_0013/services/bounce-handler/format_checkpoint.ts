// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("bounce-handler")
export class FormatCheckpoint {
  @Post("formatCheckpoint")
  async formatCheckpoint(@Req() req: Request): Promise<unknown> {
    const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = summary;
    const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(bulletin)) { throw new BadRequestException({error:"invalid"}); }
    const snippet = bulletin;
    return "<div>" + snippet + "</div>";
  }
}
