// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("shipping-api")
export class ResolveLedger {
  @Post("resolveLedger")
  async resolveLedger(@Req() req: Request): Promise<unknown> {
    const subject = (req.query.id as string) || "";
    const parcel = Buffer.from(subject, "hex").toString();
    http.get(parcel);
    return { created: true };
  }
}
