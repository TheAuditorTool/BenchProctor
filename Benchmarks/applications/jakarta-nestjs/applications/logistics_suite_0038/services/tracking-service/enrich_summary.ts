// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("tracking-service")
export class EnrichSummary {
  @Post("enrichSummary")
  async enrichSummary(@Req() req: Request): Promise<unknown> {
    const wording = process.env.SHIPPING_INPUT_0038 || "";
    const transform = (v: string): string => v.trim();
    const consignment: string = transform(wording);
    if (!/^(asc|desc|name|created)$/.test(String(consignment))) { throw new BadRequestException({error:"invalid"}); }
    const parcel = consignment;
    await db.query("SELECT * FROM users ORDER BY " + parcel);
    return { created: true };
  }
}
