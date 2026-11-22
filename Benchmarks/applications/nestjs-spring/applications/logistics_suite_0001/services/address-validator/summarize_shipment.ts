// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("address-validator")
export class SummarizeShipment {
  @Post("summarizeShipment")
  async summarizeShipment(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers.host as string) || "";
    const parcel = `${quotation}`;
    http.get(parcel);
    return { created: true };
  }
}
