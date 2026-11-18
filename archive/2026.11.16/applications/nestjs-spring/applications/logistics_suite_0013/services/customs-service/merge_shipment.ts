// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("customs-service")
export class MergeShipment {
  @Post("mergeShipment")
  async mergeShipment(@Req() req: Request): Promise<unknown> {
    const footnote = (req.query.id as string) || "";
    const parcel = Buffer.from(footnote, "hex").toString();
    http.get(parcel);
    return { created: true };
  }
}
