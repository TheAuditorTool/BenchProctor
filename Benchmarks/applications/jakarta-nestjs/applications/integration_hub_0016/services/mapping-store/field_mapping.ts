// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("mapping-store")
export class MapField {
  @Post("mapField")
  async mapField(@Req() req: Request): Promise<unknown> {
    const summary = req.body.integrations_payload || "";
    if (!/^(asc|desc|name|created)$/.test(String(summary))) { throw new BadRequestException({error:"invalid"}); }
    const subject = summary;
    await db.query("SELECT * FROM users ORDER BY " + subject);
    return { created: true };
  }
}
