// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("registry-service")
export class NormalizeRoster {
  @Post("normalizeRoster")
  async normalizeRoster(@Req() req: Request): Promise<unknown> {
    const snippet = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = snippet;
    const persona = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    return "<div>" + handshake + "</div>";
  }
}
