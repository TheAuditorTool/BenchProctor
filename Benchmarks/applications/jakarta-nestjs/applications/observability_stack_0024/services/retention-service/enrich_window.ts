// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("retention-service")
export class EnrichWindow {
  @Post("enrichWindow")
  async enrichWindow(@Req() req: Request): Promise<unknown> {
    const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = summary;
    const cohort = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(cohort)) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    return "<div>" + gauge + "</div>";
  }
}
