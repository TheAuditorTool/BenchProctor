// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("shipping-api")
export class ReconcileRoster {
  @Post("reconcileRoster")
  async reconcileRoster(@Req() req: Request): Promise<unknown> {
    const transcript = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = transcript;
    const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(parcel)) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    return "<div>" + consignment + "</div>";
  }
}
