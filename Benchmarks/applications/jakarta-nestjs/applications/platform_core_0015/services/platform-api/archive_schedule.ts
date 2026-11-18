// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("platform-api")
export class ArchiveSchedule {
  @Post("archiveSchedule")
  async archiveSchedule(@Req() req: Request): Promise<unknown> {
    const note = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = note;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { throw new BadRequestException({error:"invalid"}); }
    const persona = handshake;
    return "<div>" + persona + "</div>";
  }
}
