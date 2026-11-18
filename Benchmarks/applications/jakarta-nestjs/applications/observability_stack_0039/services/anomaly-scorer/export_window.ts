// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("anomaly-scorer")
export class ExportWindow {
  @Post("exportWindow")
  async exportWindow(@Req() req: Request): Promise<unknown> {
    const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = caption;
    const cohort = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(cohort)) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    return "<div>" + gauge + "</div>";
  }
}
