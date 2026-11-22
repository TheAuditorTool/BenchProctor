// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("carrier-gateway")
export class CollectLabel {
  @Post("collectLabel")
  async collectLabel(@Req() req: Request): Promise<unknown> {
    const quotation = (req.query.id as string) || "";
    const parcel = Buffer.from(quotation, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [parcel]);
    return { created: true };
  }
}
